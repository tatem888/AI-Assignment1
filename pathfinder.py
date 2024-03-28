import numpy as np
import sys

#open map file, split lines into Map SIze, start point and end point tuple, and map data 2d array


with open(sys.argv[1], "r") as mapFile:

    mapSize = tuple(map(int,mapFile.readline().split()))
    startPoint = tuple(map(int,mapFile.readline().split()))
    endPoint = tuple(map(int,mapFile.readline().split()))

    mapData = np.zeros(mapSize)

    #itterate through each line of mapFile, adding to mapData array, treating 'X's as -1 (impassable)
    for i in range(mapSize[0]):
        
        elements = mapFile.readline().split()

        for j in range(mapSize[1]):
            
            if elements[j] == "X":
                mapData[i,j] = -1
            else:
                mapData[i,j] = int(elements[j])

    #pad border with -1s (impassable)
    mapData = np.pad(mapData, (1,1), mode='constant', constant_values=(-1,-1))

#read algorithm and heuristic from command line

algorithm = sys.argv[2]

def bfs(startPoint, endPoint, mapData):

def ucs(startPoint, endPoint, mapData):

def astar(startPoint, endPoint, mapData, heuristic):


if algorithm == "bfs":          #breadth first search
    bfs(startPoint, endPoint, mapData)

elif algorithm == "ucs":          #uniform cost search
    ucs(startPoint, endPoint, mapData)

elif algorithm == "astar":        #astar search
    heuristic = sys.argv[3]
    astar(startPoint, endPoint, mapData, heuristic)

else:
    raise TypeError ("Invalid argument type")

print(algorithm)
print(heuristic)
print(mapData)

