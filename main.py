from PIL import Image
from numpy import *
import math
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
    
    return width, height, bmp_array[::-1]

image = "map2.bmp"
pixelated_image = "pixel2.bmp"
pixel_size = 20

pixelate(image, pixel_size, pixelated_image)
width, height, bmp_array = bmp_to_array(pixelated_image, pixel_size)

print(width, height)

def array_to_bmp(width, height, bmp_array, file_name):
    framebuffer = [[0 for _ in range(width)] for _ in range(height)]
    bmp_array_len = len(bmp_array)
    pixel_ratio = width // len(bmp_array)

    for i in range(width):
        for j in range(height):
            x, y = i // pixel_ratio, j // pixel_ratio
            if (x == bmp_array_len): x = bmp_array_len - 1
            if (y == bmp_array_len): y = bmp_array_len - 1
            if (bmp_array[x][y] == 0):
                framebuffer[i][j] = bytes([0, 0, 0])
            elif (bmp_array[x][y] == 1):
                framebuffer[i][j] = bytes([255, 255, 255])
            elif (bmp_array[x][y] == 8):
                framebuffer[i][j] = bytes([255, 0, 0])
            elif (bmp_array[x][y] == 9):
                framebuffer[i][j] = bytes([0, 255, 0])
            elif (bmp_array[x][y] == 5):
                framebuffer[i][j] = bytes([0, 0, 255])

    bmp.write_bmp(file_name, framebuffer[::-1], width, height)
