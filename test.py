import numpy as np
import sys

#open map file, split lines into Map SIze, start point and end point tuple, and map data 2d array


mapFile = """10 10
    1 1
    10 10
    1 1 1 1 1 1 4 7 8 X
    1 1 1 1 1 1 1 5 8 8
    1 1 1 1 1 1 1 4 6 7
    1 1 1 1 1 X 1 1 3 6
    1 1 1 1 1 X 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    6 1 1 1 1 X 1 1 1 1
    7 7 1 X X X 1 1 1 1
    8 8 1 1 1 1 1 1 1 1
    X 8 7 1 1 1 1 1 1 1"""

mapSize = tuple(map(int,mapFile.readline().split()))
startPoint = tuple(map(int,mapFile.readline().split()))
endPoint = tuple(map(int,mapFile.readline().split()))

mapData = np.zeros(mapSize)

for i in range(mapSize[0]):
        
    elements = mapFile.readline().split()

    for j in range(mapSize[1]):
            
        if elements[j] == "X":
            mapData[i,j] = -1
        else:
            mapData[i,j] = elements[j]

print(mapData)