from PIL import Image
from numpy import *
import bmp

def pixelate(input_file_path, pixel_size, file_name):
    image = Image.open(input_file_path)

    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )

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

def bmp_to_array(input_file_path, pixel_size):
    bmp_array = []
    width, height, pixels = bmp.read_bmp(input_file_path)

    for i in range(0, height, pixel_size):
        new_row = []
        for j in range(0, width, pixel_size):
            color = int.from_bytes(pixels[i][j], "little")
            if (color == 16_777_215):
                new_row.append(1)
            elif (color == 0):
                new_row.append(0)
            elif (color < 10_000_000):
                new_row.append(9)
            else:
                new_row.append(8)
        bmp_array.append(new_row)
    
    return bmp_array[::-1]


pixelate("map2.bmp",20,"pixel2.bmp")
bmp_array = bmp_to_array("pixel2.bmp", 20)

for row in bmp_array:
    print(row)
