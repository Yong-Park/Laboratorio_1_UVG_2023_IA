from PIL import Image
from numpy import *
import bmp
from dfs import *
from A_fCost import *

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
    
    return bmp_array[::-1]

image = "map1.bmp"
pixel_size = 35
pixel_image = "pixel1.bmp"

pixelate(image,pixel_size,pixel_image)
bmp_array = bmp_to_array(pixel_image, pixel_size)

for y in bmp_array:
    print(y)

# dfs = DFS(bmp_array)
# dfs_laberinto,dfs_visited = dfs.Start()
# print("el resultado final es")
# print(dfs_laberinto)
# print("visitados")
# print(dfs_visited)

afcost = Fcost_A(bmp_array)
afcost.algorithm()
Fcost_A_camino = afcost.camino
print("camino final: ", Fcost_A_camino)
