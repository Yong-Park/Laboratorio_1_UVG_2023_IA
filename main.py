from PIL import Image
from numpy import *

def pixelate(input_file_path, pixel_size,file_name):
    image = Image.open(input_file_path)
    
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    # d = image.getdata()
    # counter = 0
    # for item in d:
    #     print(item)
    #     counter +=1
    # print(counter)
    
    
    image = image.convert("RGB")
    
    d = image.getdata()
    
    new_image = []
    
    for item in d:
   
        if item[0] in list(range(200, 256)) and item[1] in list(range(200, 256)) and item[2] in list(range(200, 256)):
            new_image.append((255, 255, 255))
        elif item[0] in list(range(0, 201)) and item[1] in list(range(0, 201)) and item[2] in list(range(0, 201)):
            new_image.append((0, 0, 0))
        else:
            new_image.append(item)
            
    image.putdata(new_image)
    
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )

    image.save(file_name)


def pixelImage(input_file_path,pixel_size):
    image = Image.open(input_file_path)
    width, height = image.size
    
    
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    
    pixel_values = list(image.getdata())
    
    for x in pixel_values:
        if (x!= (0,0,0)):
            if(x!= (255,255,255)):
                print(x)
                print("===")
                
def processMaze (input_file_path,pixel_size):
    image = Image.open(input_file_path)
    
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    pixel_values = list(image.getdata())
    maze = []
    for mazeRow in pixel_values:
        tempMazeRow = []
        if mazeRow == (255, 255, 255):
            tempMazeRow.append('#')
        elif mazeRow == (0, 0, 0):
            tempMazeRow.append(" ")
        maze.append(tempMazeRow)
    return maze
    
pixelate("map2.bmp",20,"pixel2.bmp")
pixelImage("pixel2.bmp",20)
# maze = processMaze("pixel2.bmp",20)
# print(maze)
