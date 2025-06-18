from PIL import Image
from urllib.request import urlopen, HTTPError
from typing import NoReturn
import sys, os, re

def convert_image(image_input: Image, path: str) -> NoReturn:
    """
        Function for converting the image to text directly
        @params
        image_input: PIL.Image
            The image which will be converted to text art

        path: str
            The output path to the text art
    """
    
    # Set of chars to generate the text art
    ## The predefined is recommended, because of the diversity and compatibility 
    charset = " _.:-=+*%#@"
    
    concat_char : str = ""
    output_text: str = ""
    
    # 255 the highest possible value 
    # 255 Divided by the charset length to get the range value between each character
    range_char: int = 255 // len(charset) 

    # A list with all intervals
    range_list: list = [range_char * i for i in range(len(charset))]

    for index, px_tuple in enumerate(image_input.getdata()):
        # If last pixel should go to a newline
        if (index % image_input.width == 0 and index != 0): 
            output+="\n"            
            
        # RGB Channel Values in tuple
        rgb = px_tuple[0:-1]
        
        # Alpha Channel Value
        alpha_ch = px_tuple[-1]

        # If alpha channel is 0 automatically concat_char is certainly charset[0]
        if (alpha_ch > 0):
            # Average of the RGB Channels
            avg_ch = sum(rgb) // 3

            # For loop for finding the best character for the given pixel
            for val in range_list:
                if abs(avg_ch - val) < abs(avg_ch - range_list[0]):
                    concat_char = charset[range_list.index(val)]
        else:
            concat_char = charset[0]

        output_text += concat_char
    
    output_file_name: str = f"{os.path.basename(os.path.splitext(path)[0])}.out.txt"
    output_file = open(output_file_name, "w+")
    output_file.writelines(output_text)

    print(f"\nThe image was processed succefully! Check out:\n- {os.path.abspath(output_file_name)}\n")

def validate(path:str, output_size:int = 1) -> None:
    """
        Function for converting the image to text directly
        @params
        path: str
            The path for the image you want to convert

        output_size: int = 1
            How many times it will divide the image initial size to the output size
            Example:
                An image with a width of 800px, and height of 600px. With a image_size of 2, the output would have 400 characters by 300 characters
                
    """
    try:
        # Regular Expression for URLs
        URL_REGEX: str = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
        
        input_image: Image
        processed_image: Image

        path_to_image = path
        if (re.match(URL_REGEX, path)):
            path_to_image = urlopen(path)

        input_image = Image.open(path_to_image)

        # Convert the each pixel to 
        input_image = input_image.convert('RGBA')
        
        if (output_size in [0,1]):
            processed_image = input_image.resize((input_image.width, input_image.height))

        else: 
            # Dividing the input_image width and height to 
            output_width: int = input_image.width // output_size
            output_height: int = input_image.height // output_size

            processed_image = input_image.resize((output_width, output_height))

        # Convert Image to Text
        convert_image(processed_image, path)
        
    except OSError:
        raise OSError("Reqested file not found")
    except HTTPError:
        raise HTTPError("The requested URL is invalid")

if __name__ == "__main__":
    if (len(sys.argv) >= 2): 
        path: str = sys.argv[1]
        if (len(sys.argv) == 2): 
            validate(sys.argv[1])
        else: 
            try:
                output_size: int = abs(int(sys.argv[2]))
                validate(path, output_size)
            
            except ValueError:
                raise ValueError("Second value needs to be an integer")
    else:
        msg: str = """
For running the program properly run
$ python main.py image_path output_size.

- image_path: 
    - An URL or a Path to an Image file.

- output_size: 
    - The fraction of the original size for the output, default value as 1 (Original Size) not reccomended
"""
        print(msg)
    pass
