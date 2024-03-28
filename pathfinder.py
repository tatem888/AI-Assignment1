import numpy as np
import sys

#open map file, split lines into Map SIze, start point and end point tuple, and map data 2d array


with open(sys.argv[1], "r") as mapFile:

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
                mapData[i,j] = int(elements[j])

#read algorithm and heuristic from command line

algorithm = sys.argv[2]

if len(sys.argv)[3] == 3:
    heuristic = sys.argv[3]

print(algorithm)
print(heuristic)
print(mapData)

