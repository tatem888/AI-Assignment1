import numpy as np
import sys

#open map file, split lines into Map SIze, start point and end point tuple, and map data 2d array


with open(sys.argv[1], "r") as mapFile:

    mapSize = tuple(map(int,mapFile.readline().split()))
    startPoint = tuple(map(int,mapFile.readline().split()))
    endPoint = tuple(map(int,mapFile.readline().split()))

    mapData = np.zeros(mapSize)

    for i in range(mapSize[0]):
        
        mapData[i,:] = mapFile.readline().split()
    
    
#read algorithm and heuristic from command line

algorithm = sys.argv[2]
heuristic = sys.argv[3]


