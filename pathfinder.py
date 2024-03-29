import numpy as np
import sys
import queue as Queue

#open map file, split lines into Map SIze, start point and end point tuple, and map data 2d array

def readFile():
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

    if algorithm == "astar":
        heuristic = sys.argv[3]
    else:
        heuristic = None

    return (mapSize,startPoint,endPoint,mapData,algorithm, heuristic)
    

#implement a node data structure
class Node: 
    def __init__(self, coordinates, elevation, parent=None):
        self.coordinates = coordinates
        self.parent = parent
        self.elevation = elevation

    def get_parent(self):
        return self.parent
    
    def get_coordinates(self):
        return self.coordinates
    
    def get_elevation(self):
        return self.elevation
    

#function to initilise the start node
def initStartNode(startPoint, mapData):

    a = startPoint[0]
    b = startPoint[1]
    
    node = Node(startPoint,mapData[a,b])

    return node
#function to initilise fringe queue
def initFringe(startNode):
    q = Queue(maxsize=0)
    q.put(startNode)
    return q

#function to initilise closed set for searched coordinates
def initClosed(mapSize, startNode):
    arr = np.zeros(mapSize)
    arr[Node.get_coordinates(startNode)] = 1
    return arr

#function to check if endpoint has been reached
def endCheck(currentNode, endPoint):
    a = currentNode.get_coordinates()
    if a == endPoint:
        return True
    else:
        return False

#function to generate nodes succeeding the state node and add them to fringe
def expandFringe(stateNode, mapData, fringe, closed):

    coords = stateNode.get_coordinates()
    x,y = coords

    up = (x, y-1)
    down = (x, y+1)
    left = (x-1, y)
    right = (x+1, y)

    if mapData[up] != -1:
        u = Node((x,y-1),mapData[up],stateNode)
        fringe.put(u)

    elif mapData[down] != -1:
        d = Node((x,y+1),mapData[down],stateNode)
        fringe.put(d)

    elif mapData[left] != -1:
        l = Node((x-1,y),mapData[left],stateNode)
        fringe.put(l)
    
    elif mapData[right] != -1:
        r = Node((x+1,y),mapData[r],stateNode)
        fringe.put(r)

    return fringe

#implementation of the graph search pseudocode
def graphSearch(startPoint, endPoint, mapData, mapSize):
    
    startNode = initStartNode(startPoint,mapData)
    closed = initClosed(mapSize, startNode)
    fringe = initFringe(startNode)

    #run until fringe is empty or return triggered
    while fringe:          
        
        if fringe.empty() == True:
            return print("null")
        
        stateNode = fringe.get()

        if endCheck(stateNode, endPoint) == True:
            return stateNode
        
        if closed[stateNode.get_coordinates] != 1:
            closed[stateNode.get_coordinates] = 1
            expandFringe(stateNode,mapData,fringe,closed)

#run function

mapSize,startPoint,endPoint,mapData,algorithm, heuristic = readFile()

a = graphSearch(startPoint,endPoint,mapData,mapSize)

print(a.get_coordinates)
print(a.get_elevation)
