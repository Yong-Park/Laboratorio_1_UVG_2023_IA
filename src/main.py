import utils
from bfs import *
from dfs import *
from dfs_backup import *
from A_fCost import *

image = "./images/map2.bmp"
pixelated_image = "./images/pixel2.bmp"
pixel_size = 20

utils.pixelate(image, pixel_size, pixelated_image)
width, height, bmp_array = utils.bmp_to_array(pixelated_image, pixel_size)

dfs = DFS(bmp_array)
dfs.actions()
visitado, camino = dfs.results()
# print(visitado)
print(camino)
road = camino

# a_star = Fcost_A(bmp_array)
# a_star.actions()
# visited, road = a_star.results()

# bfs = BFS(bmp_array)
# road = bfs.search_shortest_path()

for point in road:
    i, j = point
    bmp_array[j][i] = 5

utils.array_to_bmp(width, height, bmp_array, "./images/result.bmp")

# afcost = Fcost_A(bmp_array)
# afcost.actions()
# visitado,camino = afcost.results()
# print("camino final resultado: ", camino)
