from PIL import Image
from numpy import *

def pixelate(input_file_path, pixel_size,file_name):
    image = Image.open(input_file_path)
    
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    d = image.getdata()
    counter = 0
    for item in d:
        print(item)
        counter +=1
    print(counter)
    
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    
    
    image = image.convert("RGB")
    
    d = image.getdata()
    
    new_image = []
    
    for item in d:
   
        if item[0] in list(range(200, 255)) and item[1] in list(range(200, 255)) and item[2] in list(range(200, 255)):
            new_image.append((255, 255, 255))
        elif item[0] in list(range(0, 200)) and item[1] in list(range(0, 200)) and item[2] in list(range(0, 200)):
            new_image.append((0, 0, 0))
        else:
            new_image.append(item)
            
    image.putdata(new_image)

    image.save(file_name)


def pixelImage(input_file_path):
    image = Image.open(input_file_path)
    width, height = image.size
    pixel_values = list(image.getdata())
    
    for x in pixel_values:
        if (x[0]!= 0 and x[1]!= 0 and x[2]!=0):
            if(x[0]!= 255 and x[1]!= 255 and x[2]!=255):
                print(x)
                print("===")
            
    
    # if image.mode == "RGB":
    #     channels = 3
    # elif image.mode == "L":
    #     channels = 1
    # else:
    #     print("Unknown mode: %s" % image.mode)
    #     return None
    # pixel_values = array(pixel_values).reshape((width, height, channels))
    # return pixel_values
    
pixelate("map1.bmp",35,"pixel1.bmp")
# pixelImage("pixel2.bmp")
