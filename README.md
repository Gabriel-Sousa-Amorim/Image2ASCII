# [Image2ASCII](https://github.com/Gabriel-Sousa-Amorim/Image2ASCII/)

A Python Learning Project, that recreates an image with text, commonly known as ASCII art.

### Requirements

- Python 3.4+ (recommended Python 3.4 or later)
- Pip (required if using Python below 3.4)
- Git (optional for cloning the repository)

## Installation

1. Clone the repository or download the source code:

```sh
git clone https://github.com/Gabriel-Sousa-Amorim/Image2ASCII.git
```

2. Navigate to the project directory:

```sh
cd Image2ASCII
```

3. Install requirements:

```
pip install -r requirements.txt
```

## Usage

To generate ASCII art from an image, run the following command:

```sh
python3 main.py <path_to_img> <size>
```
- Replace <path_to_img> with the path to your image file (local or URL). Note: URL images may cause 403 and 404 errors.
- Replace <size> with a divisor for the image dimensions. 

> For example, if the image is 1000x1000 and you want a 500x500 ASCII output, set the size to 2.

```sh
python3 main.py ./images/sample.jpg 2
```

## Running Tests

Check the [tests/](./tests/) folder for example outputs.


```
              ++              
              ++              
             =++=             
             ++++             
             ++++             
            *+##+*            
            ++ÑÑ++            
            +*ÑÑ*+            
           ==#ÑÑ#==           
%==%%%%%%%%++ÑÑÑÑ++%%%%%%%%==%
++++++======*ÑÑÑÑ*======+++++%
 *+++%Õ@@@@@ÑÑÑÑÑÑ@@@@@Õ%+++* 
   ++*ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ*++   
    +++#ÑÑÑÑÑÑÑÑÑÑÑÑÑÑ#+++    
      ++*ÑÑÑÑÑÑÑÑÑÑÑÑ*++      
       +++ÕÑÑÑÑÑÑÑÑÕ+++       
        ++*ÑÑÑÑÑÑÑÑ*++        
        ==@ÑÑÑÑÑÑÑÑ@==        
        ++ÑÑÑÑÑÑÑÑÑÑ++        
        +*ÑÑÑÑ%%ÑÑÑÑ*+        
       ==#ÑÑÕ++++ÕÑÑ#==       
       ++ÑÑ%+++*++%ÑÑ++       
       ++@*++    ++*@++       
       +++++      +++++       
      ++++          ++++      
      +++            +++      
      +%              %+      
```
