import sys #import sys to read arguments from command line
from Vertex import Vertex #import Vertex class from Vertex.py file
from Graph import Graph #import Graph class from Graph.py file

#first argument contains the network information
#second argument contains the queries to be run on the network
#third argument is the output file which contains output after queries are run
networkFile = open(sys.argv[1], mode='r') 
queriesFile = open(sys.argv[2], mode='r')
outputFile = open(sys.argv[3], mode='w')

#create a graph object
graph = Graph()
for edge in networkFile:
    print("  -->", edge, end='')
    edge = edge.split()
    graph.addEdge(edge[0],edge[1],edge[2],"UP")
    graph.addEdge(edge[1],edge[0],edge[2],"UP")

#read and execute queries from query file(second argument)
for query in queriesFile:
    print("  -->",query, end='')
    query = query.split()
    if query[0] == 'addedge':
        graph.addEdge(query[1], query[2], query[3], "UP")
    elif query[0] == 'deleteedge':
        graph.deleteEdge(query[1], query[2])
    elif query[0] == 'edgeup':
        graph.edgeUp(query[1], query[2])
    elif query[0] == 'edgedown':
        graph.edgeDown(query[1], query[2])
    elif query[0] == 'vertexup':
        graph.vertexUp(query[1])
    elif query[0] == 'vertexdown':
        graph.vertexDown(query[1])
    elif query[0] == 'print':
        graph.printGraph(outputFile)
    elif query[0] == 'reachable':
        graph.reachable(outputFile)
    elif query[0] == 'path':
        graph.reset()
        #if either vertex is down, print Not reachable
        if graph.verticesStatus[query[1]] == "DOWN" or graph.verticesStatus[query[2]] == "DOWN":
            print("Not reachable",file=outputFile)
        #else, run the Dijkstras algorithm to find the shortest path
        else:
            graph.dijkstras(graph.getVertex(query[1]), graph.getVertex(query[2]))
            destination = graph.getVertex(query[2])
            path = [destination.getId()]
            graph.shortestPath(destination, path)
            print(*path[::-1], "{0:.2f}".format(destination.distance),sep=" ",file=outputFile)
    elif query[0] == 'quit':
        print("\n> Exiting program")
        break;        

print("\n> Find output in file ",sys.argv[3])
networkFile.close()
queriesFile.close()
outputFile.close()

