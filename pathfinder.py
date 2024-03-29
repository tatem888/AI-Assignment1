import numpy as np
import sys
from queue import Queue
from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any



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
    
    
    
@dataclass(order=True)
class PrioritisedItem:
    def __init__(self,priority, node):
        self.priority = priority
        self.node = node

    priority: int
    node: Any=field (compare=False)

    def get_node(self):
        return self.node



#function to initilise the start node
def initStartNode(startPoint, mapData):

    a = startPoint[0]
    b = startPoint[1]
    
    node = Node(startPoint,mapData[a,b])

    return node
#function to initilise fringe queue
def initFringe(startNode):
    q = Queue(maxsize = 50)
    q.put(startNode)
    return q

def initPriorityFringe(startPriorityItem):
    q = PriorityQueue(maxsize = 50)
    q.put(startPriorityItem)
    return q

#function to initilise closed set for searched coordinates
def initClosed(mapSize):
    arr = np.zeros(mapSize)
    arr = np.pad(arr, (1,1), mode='constant',constant_values=(1,1))
    return arr

#function to check if endpoint has been reached
def endCheck(currentNode, endPoint):
    a = Node.get_coordinates(currentNode)
    if a == endPoint:
        return True
    else:
        return False

#function to generate nodes succeeding the state node and add them to fringe
def expandFringe(stateNode, mapData, fringe, closed):

    coords = Node.get_coordinates(stateNode)
    x,y = coords

    up = (x-1, y)
    down = (x+1, y)
    left = (x, y-1)
    right = (x, y+1)

    if mapData[up] != -1 and closed[up] != 1:
        u = Node((x-1,y),mapData[up],stateNode)
        fringe.put(u)

    if mapData[down] != -1 and closed[down] != 1:
        d = Node((x+1,y),mapData[down],stateNode)
        fringe.put(d)
        
    if mapData[left] != -1 and closed[left] != 1:
        l = Node((x,y-1),mapData[left],stateNode)
        fringe.put(l)

    if mapData[right] != -1 and closed[right] != 1:
        r = Node((x,y+1),mapData[right],stateNode)
        fringe.put(r)
        
    return fringe

#implementation of the graph search pseudocode
def bfsGraphSearch(startPoint, endPoint, mapData, mapSize):
    
    startNode = initStartNode(startPoint,mapData)
    closed = initClosed(mapSize)
    fringe = initFringe(startNode)


    #run until fringe is empty or return triggered
    while fringe:          
        
        if fringe.empty() == True:
            return print("null")
        
        stateNode = fringe.get()

        if endCheck(stateNode, endPoint) == True:
            return stateNode
        
        if closed[Node.get_coordinates(stateNode)] != 1:
            closed[Node.get_coordinates(stateNode)] = 1
            expandFringe(stateNode,mapData,fringe,closed)


def uscExpandFringe(stateNode, mapData, fringe, closed):

    coords = Node.get_coordinates(stateNode)
    x,y = coords

    up = (x-1, y)
    down = (x+1, y)
    left = (x, y-1)
    right = (x, y+1)

    if mapData[up] != -1 and closed[up] != 1:
        u = Node((x-1,y),mapData[up],stateNode)
        up = PrioritisedItem(Node.get_elevation(u),u)
        fringe.put(up)

    if mapData[down] != -1 and closed[down] != 1:
        d = Node((x+1,y),mapData[down],stateNode)
        dp = PrioritisedItem(Node.get_elevation(d),d)
        fringe.put(dp)
        
    if mapData[left] != -1 and closed[left] != 1:
        l = Node((x,y-1),mapData[left],stateNode)
        lp = PrioritisedItem(Node.get_elevation(l),l)
        fringe.put(lp)

    if mapData[right] != -1 and closed[right] != 1:
        r = Node((x,y+1),mapData[right],stateNode)
        rp = PrioritisedItem(Node.get_elevation(r),r)
        fringe.put(rp)
        
    return fringe

def ucsGraphSearch(startPoint, endPoint, mapData, mapSize):
    
    startNode = initStartNode(startPoint,mapData)
    startPriorityItem = PrioritisedItem(1,startNode)
    closed = initClosed(mapSize)
    fringe = initPriorityFringe(startPriorityItem)

    #run until fringe is empty or return triggered
    while fringe:          
        
        if fringe.empty() == True:
            return print("null")
        
        priorityItem = fringe.get()
        stateNode = PrioritisedItem.get_node(priorityItem)


        if endCheck(stateNode, endPoint) == True:
            return stateNode
        
        if closed[Node.get_coordinates(stateNode)] != 1:
            closed[Node.get_coordinates(stateNode)] = 1
            uscExpandFringe(stateNode,mapData,fringe,closed)

def outputMap(endNode, mapData, mapSize):

    outputArray = mapData
    while Node.get_parent(endNode) != None:
    
        coords = Node.get_coordinates(endNode)
        outputArray[coords] = -2
        endNode = Node.get_parent(endNode)
    
    outputArray[Node.get_coordinates(endNode)] = -2

    a,b = mapSize

    for x in range(1,a+1):
        for y in range(1,b+1):
            if outputArray[x,y] == -2:
                print("*",end=" ")
            elif outputArray[x,y] == -1:
                print("X",end=" ")
            else:
                print(int(outputArray[x,y]),end=" ")
        print()
#run function
mapSize,startPoint,endPoint,mapData,algorithm, heuristic = readFile()

if algorithm == "bfs":
    endNode = bfsGraphSearch(startPoint,endPoint,mapData,mapSize)
elif algorithm == "ucs":
    endNode = ucsGraphSearch(startPoint,endPoint,mapData,mapSize)

outputMap(endNode,mapData,mapSize)


