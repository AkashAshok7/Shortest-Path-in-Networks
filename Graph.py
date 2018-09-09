#importing classes
import sys
from PriorityQueue import PriorityQueue
from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertices = {} #initializing the dictionary for vertices
        self.verticesStatus = {} #initializing the dictionary for the status of the vertices

    #initially all vertices will be UP
    def addVertex(self, node):
        newVertex = Vertex(node)
        self.vertices[node] = newVertex
        self.verticesStatus[node] = "UP"
        return newVertex
    
    def getVertex(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return None

    def addEdge(self, source, destination, transmissionTime, status):
        if source not in self.vertices:
            self.addVertex(source)
        if destination not in self.vertices:
            self.addVertex(destination)
        self.vertices[source].addNeighbor(self.vertices[destination], transmissionTime, status)

    def deleteEdge(self, source, destination):
        self.vertices[source].adjacent.pop(destination)

    #mrking the edges and vertices UP and DOWN to show their status
    def edgeUp(self, source, destination):
        self.vertices[source].adjacent[destination][1]="UP"

    def edgeDown(self, source, destination):
        self.vertices[source].adjacent[destination][1]="DOWN"
       
    def vertexUp(self,vertex):
        self.verticesStatus[vertex] = "UP"
       
    def vertexDown(self,vertex):
        self.verticesStatus[vertex] = "DOWN"

    #printing the vertices and thier status in the output_file
    def printGraph(self, outputFile):
        for vertex in sorted(list(self.vertices)):
            print(vertex, self.verticesStatus[vertex], file=outputFile)
            for node in sorted(list(self.vertices[vertex].adjacent.keys())):
                        print("  ",node,self.vertices[vertex].adjacent[node][0],self.vertices[vertex].adjacent[node][1], file=outputFile)

    def pathExists(self, source, destination, path = []):
        path = path + [source]
        if source == destination:
            return True
        if source not in self.vertices:
            return False
        for node in self.vertices[source].adjacent:
            if node not in path and  self.vertices[source].adjacent[node][1]=="UP":
                newpath = self.pathExists(node, destination, path)
                if newpath: return True
        return False


    def reachable(self, outputFile):
        #for every vertex
        for vertex in sorted(list(self.vertices.keys())):
            if self.verticesStatus[vertex]=="UP":
                print(vertex, file=outputFile)
                for node in sorted([key for key in list(self.vertices.keys()) if key != vertex]):
                    if self.pathExists(vertex, node):
                        print("  ",node, file=outputFile)
     
    #implementation of Dijkstras Algorithm using priority queues
    def dijkstras(self, source, destination):
        priorityQueue = PriorityQueue() 
        source.setDistance(0)
        unvisitedQueue = [(self.vertices[v].getDistance(),self.vertices[v].getId()) for v in self.vertices if self.verticesStatus[v]=="UP"]
        priorityQueue.buildPQ(unvisitedQueue) 
        while len(priorityQueue)-1:
            closestVertex = priorityQueue.deleteMinimum()
            closestVertex = self.getVertex(closestVertex[1])
            closestVertex.setVisited()
            for nextVertex in closestVertex.adjacent: 
                #checking if both the vertex and the edge are UP
                if self.verticesStatus[nextVertex]=="UP" and closestVertex.adjacent[nextVertex][1]=="UP":
                    nextVertex = self.getVertex(nextVertex)
                    if nextVertex.visited:
                        continue
                    newDistance = closestVertex.getDistance() + float(closestVertex.getWeight(nextVertex.id)) #update distance
                    if newDistance < nextVertex.getDistance():
                        nextVertex.setDistance(newDistance) #update distance
                        nextVertex.setPrevious(closestVertex)
                        
            while len(priorityQueue)-1:
                priorityQueue.deleteMinimum()
            unvisitedQueue = [(self.vertices[v].getDistance(),self.vertices[v].getId()) for v in self.vertices if not self.vertices[v].visited]
            priorityQueue.buildPQ(unvisitedQueue)

    def shortestPath(self, target, path):
        if target.previous:
            path.append(target.previous.getId())
            self.shortestPath(target.previous, path)
        return
    
    def reset(self):
        for vertex in self.vertices:
            self.vertices[vertex].setUnvisited()
            self.vertices[vertex].previous=None
            self.vertices[vertex].setDistance(sys.maxsize) 
