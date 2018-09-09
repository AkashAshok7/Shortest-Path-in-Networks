import sys
class Vertex:
    def __init__(self, name):
        self.id = name
        self.adjacent = {}
        self.distance = sys.maxsize
        # all nodes are initially not visited    
        self.visited = False  
        # none of the nodes have any parents/predecessors
        self.previous = None

    #add neighbor to adjacency list of vertex
    def addNeighbor(self, neighbor, weight, status):
        self.adjacent[neighbor.id] = [weight, status]


    #Getters and Setters     
        
    #get Id of vertex
    def getId(self):
        return self.id
    
    #get weight of vertex
    def getWeight(self, neighbor):
        return self.adjacent[neighbor][0]

    #set distance attribute of vertex
    def setDistance(self, dist):
        self.distance = dist

    #get distance of vertex
    def getDistance(self):
        return self.distance

    #set predecessor of vertex
    def setPrevious(self, prev):
        self.previous = prev

    #set vertex to visited
    def setVisited(self):
        self.visited = True
        
    #set vertex to unvisited
    def setUnvisited(self):
        self.visited = False
