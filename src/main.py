import utils
from bfs import *
from dfs import *
from dfs_backup import *
from A_fCost import *
from degree_a_star import *

image = "./images/turing.bmp"
pixelated_image = "./images/pixel_turing.bmp"
pixel_size = 1

utils.pixelate(image, pixel_size, pixelated_image)
width, height, bmp_array = utils.bmp_to_array(pixelated_image, pixel_size)

print("""
    1. BFS.
    2. DFS.
    3. A* (euclidean).
    4. A* (inverse tangent).
""")

algorithm = input("Input the algorithm you want to use: ")

if (algorithm == "1"):
    bfs = BFS(bmp_array)
    road = bfs.search_shortest_path()
elif (algorithm == "2"):
    dfs = DFS(bmp_array)
    dfs.actions()
    visited, road = dfs.results()
elif (algorithm == "3"):
    a_star = Fcost_A(bmp_array)
    a_star.actions()
    visited, road = a_star.results()
elif (algorithm == "4"):
    a_star = DegreeAstar(bmp_array)
    a_star.actions()
    visited, road = a_star.results()
else:
    print("You didn't input a valid algorithm.")
    exit()

print("_____")
print(visited)
print()
print(road)

for point in visited[0:-2]:
    i, j = point
    if (algorithm == "1"):
        bmp_array[i][j] = 5
    else:
        bmp_array[j][i] = 5

utils.array_to_bmp(width, height, bmp_array, "./images/result.bmp")

print("\nResult's out. Check ./images/result.bmp.\n")
