# Implementation Document

## Main structure of the program

### General

Program is used through graphical user interface, which is done with TkInter. It is very simple ui, so it is in two files, ui.py handles launching of the app and start_view.py the rest. User will insert two coordinates from the map and then choose an algorithm to find the shortest path. The app will then call the algorithm from algorithms -folder and if there is a path, it will print the length of the shortest path and time it took to find it. The algorithm function returns a distance matrix that is then visualized to the user as a TkInter canvas.

### Dijkstra

The main function is find_route. Start time is taken first, then the function will call initialize -function to establish the distance matrix and neighbours -dictionary from the map. There are two for -loops to check every pixel. The function will check where the current pixel is on the map, for example if it is on the left side, it will not add any neighbour from the left side, as there is no pixel to add. After the initialize call, we know neighbours to every node and have the distance matrix with "walls" as "@" and every distance is 999.

Next the input will be checked. Nothing special here.

Now the main function will start. The start node is added to the heap. Next while loop starts and it will last as long as there are nodes in the heap. The smallest node is removed from the heap. If we have visited the smallest node already, we can continue. Unless not, we'll add the node to "visited" list. Then we will check it's neighbours, if the "new" distance is less our current distance, we'll improve the distance to the distance matrix and push the neighbour to the with the improved distance. This loop will continute until no distance can be improved.

Lastly, the shortest path can be fetched from the previous nodes and the shortest path is counted at the same time. The start time is stopped and the function will return a tuple with the distance matrix and the shortest path length.

### Ida Star

First a graph is initialized. There are nodes and their children are the neighbours. This is done with two for -loops. The heuristic is counted. This algorithm uses a "manhattan distance" as a heuristic. It is counted from the difference between the start and end node's x and y coordinates. 

A while loop is entered which will last until we have found the shortest path. The loop will call _search -function that uses recursion to find shortest distances. With each function call the threshold is updated. The _search -function will return only the new cost to reach that node if it is larger than the treshold, so it will not explore any more of it's neighbours, so time is saved. Each time the f value is less than treshold, we will explore the node's neighbours and update the cost to reach that node. 

### Heap

Heap has function to get it's length, add nodes to the heap and pop (remove and return) the smallest node.

Length is simply counted from the length of the heap list minus one, because there is "None" object to make sure the indexing is starting from 1.

Push function will add a new node to the list and then adjust the heap until the node doesn't have a smaller parent node anymore.

Pop function will remove the smallest (root) node from the heap and then make the last node as the root node. Now the heap will be adjusted until there are no more smaller parents to that node.

## Time and Space complexities
TODO

## Performance

TODO



## Sources

Tirakirja by Antti Laaksonen [https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/]

IDA* Algorithm in general by algorithmsinsight [https://algorithmsinsight.wordpress.com/graph-theory-2/ida-star-algorithm-in-general/]

Iterative deepening A* - Wikipedia [https://en.wikipedia.org/wiki/Iterative_deepening_A*]