from PIL import Image, ImageOps
from urllib.request import urlopen, HTTPError
import sys, os, re

def convertImg(im_input: Image, path: str) -> None:
    # Set of chars to generate the art recommended very diverse set
    chars : str = " _.:-=+*%#@ÕÑ"

    char_to_add : str = ""
    output: str = ""
    
    range_char: int = 255 // len(chars) # 255 the highest possible value im_input.getdata() divided char length to get the range between each character
    range_list: list = [range_char * i for i in range(len(chars))]

    for index, px_tuple in enumerate(im_input.getdata()):
        if (index % im_input.width == 0 and index != 0): output+="\n"            
        avg_px = sum(px_tuple) // 4
        # For loop for finding the best fitting character for the given obj
        for val in range_list:
            if abs(avg_px - val) < abs(avg_px - range_list[0]):
                char_to_add = chars[range_list.index(val)]
        output += char_to_add

    text_file = open(f"{os.path.basename(os.path.splitext(path)[0])}.out.txt", "w+")
    text_file.writelines(output)

def main(path:str, img_size:int = 1) -> None:
    try:
        im:Image
        out: Image
        if (re.match(r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})", path)):
            im = Image.open(urlopen(path))
        else:
            im = Image.open(path)
        if (img_size in [0,1]):
            out = im.resize((im.width, im.height))
        else: 
            out = im.resize((im.width//img_size, im.height//img_size))
        convertImg(out, path)
    except OSError:
        raise OSError("File not found")
    except HTTPError:
        raise HTTPError("Invalid Url")

if __name__ == "__main__":
    if (len(sys.argv) >= 2): 
        if (len(sys.argv) == 2): 
            main(sys.argv[1], 1)
        else: 
            try:
                main(sys.argv[1], abs(int(sys.argv[2])))
            except ValueError:
                raise ValueError("Second value needs to bee an integer")
    else:
        print("For running the program properly run\n   $ python main.py image_path img_size")
    pass
