if mapData[up] != -1 and closed[up] != 1:
        u = Node((x-1,y),mapData[up],stateNode)
        fringe.put(u)
        print(Node.get_coordinates(u),"u")

    if mapData[down] != -1 and closed[down] != 1:
        d = Node((x+1,y),mapData[down],stateNode)
        fringe.put(d)
        print(Node.get_coordinates(d),"d")

    if mapData[left] != -1 and closed[left] != 1:
        l = Node((x,y-1),mapData[left],stateNode)
        fringe.put(l)
        print(Node.get_coordinates(l),"l")

    if mapData[right] != -1 and closed[right] != 1:
        r = Node((x,y+1),mapData[right],stateNode)
        fringe.put(r)
        print(Node.get_coordinates(r),"r")