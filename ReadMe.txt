To execute the program, run the following on the terminal:
python main.py <network_file> <query file> <output_file>

The output of the query on the network file will be stored in the output_file. It will be created if no file exists or will be rewritten
if the file exists.

This project consists of 4 files:
1. Vertex.py: which contains the definition of vertex class
2. Graph.py: which contains the definition of graph class
3. PriorityQueue.py: which contains the definition for the Priority Queue
4. main.py: here, the graph is read, queries are executed and the output is written to the output file.

The graph is implemented as a dictionary which consists of the vertex object and the vertex's status (up or down).
The Priority Queue is implemented as a list.

Execution procedure:

1. Open the terminal with the path of the project directory.
2. Run the command python main.py <network_file> <query file> <output_file>
   Make sure to have all the files under the same folder.
3. Check the output_file for output of the query on the network.
4. Make changes to the network_file and the query_file text files as required.
5. Run the command once again.


Note: The network_file and the query_file should be of a given structure or format for the implementation to run correctly.
      No error handling has been done for this.