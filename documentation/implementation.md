# Implementation Document

## Main structure of the program

### General

Program is used through graphical user interface, which is done with TkInter. It is very simple ui, so it is in two files, ui.py handles launching of the app and start_view.py the rest. User will insert two coordinates from the map and then choose an algorithm to find the shortest path. The app will then call the algorithm from algorithms -folder and if there is a path, it will print the length of the shortest path and time it took to find it. The algorithm function returns a distance matrix that is then visualized to the user as a TkInter canvas.

### Dijkstra

The main function is find_route. Start time is taken first, then the function will call initialize -function to establish the distance matrix and neighbours -dictionary from the map. There are two for -loops to check every pixel. The function will check where the current pixel is on the map, for example if it is on the left side, it will not add any neighbour from the left side, as there is no pixel to add. After the initialize call, we know neighbours to every node and have the distance matrix with "walls" as "@" and every distance is 999.

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

### IDA*

#### Time complexity

IDA*'s time complexity depends on the problem and the efficiency of the heuristic. 

Our graph's branching factor is generally 4, because every node can have maximum of 4 neighbours. However when using maps with more walls, this will be less as we won't add walls as neighbours.

The more accurate heuristic, the better is the time complexity. This works for both ways. Every time the f score is bigger than threshold, algorithm has to iterate. IDA*'s iterations are quite time consuming in a large graph and with a branching factor 4, the graph is very large.

The heuristic I implemented is Manhattan distance and it will choke especially if the map requires a lot of "steps left". This will cause many unnecessary iterations that adds up to the run time. While there are many alternatives, an accurate heuristic is difficult to choose, especially when the input is a random map.

The time complexity of IDA* IS O(b**d), where b is the branching factor and d is the depth of the found goal node. Altough there are some discussion to be had if this is the correct time complexity, in my opinion it seems accurate when comparing to my empiric results.

#### Space complexity

IDA*'s space complexity is linear to the length of the fastest route, because only the current fastest route is stored in the memory. So space complexity is O(d), where d is "the shallowest goal node".

### Dijkstra

#### Time complexity

Dijkstra will visit every coordinate and their neighbours in the map, which takes O(n + m) (n=number of nodes, m=numer of neighbours) time. Every node has maximum of 4 neighbours. In worst case scenario, the algorithm will add every node to the heap. In my opinion I implemented heap as efficiently as possible with Python, so the worst case scenario operations will take time O(mlogm). Every node that is pushed, will also be popped. This will happen in O(mlogm) too. Total time complexity will be O(n+mlogm).

#### Space complexity

The algorithm keeps a long queue of nodes in memory, which can be very taxing. Worst case scenario, every node will be at some point added to the heap, so space complexity can get to O(n+m).

## Performance

### Algorithms

With smaller and simpler maps, IDA* is consistently faster than Dijkstra. For example in 10x10 map, it is 30-50% faster. When moving to larger maps, Dijkstra is faster. For example in 15x15 map, the difference is noticeable in graph form:

![performance in 15x15 map](https://github.com/evahteri/Path-Finder/blob/main/documentation/performance_test_15x15.png)

Here we can see that Dijkstra is faster when handling longer paths. IDA* is faster at the start when zooming in, but the difference is not big. When moving to a 30x30 map, Dijkstra is usually 100% faster than IDA*

The results don't depend only on the path length. When IDA*'s heuristic's estimation is worse, the run time increases. When inspecting the slower inputs, we can see that the manhattan distance is quite far from the reality. This is why in some performance tests, Dijkstra is faster, even though a smaller map is in use. Because the inputs are random, if there is these kind of puuteinputs, where mahnattan distance is a poor estimation, Dijkstra will be noticeably faster.

All of these performance tests can be run by the user via the graphical user interface.

### Heap

I am content with the heap's performance. Altough, it isn't as efficient as Python's heapq class, it is still performing quite nicely. With 1000 push and pop calls, heapq is about 80% faster than my implementation.

### Analysis

When choosing between Dijkstra and IDA* as path finding algorithms, my results indicate that if there's no data about the map, then Dijkstra will offer a more stable performance. If we know some characteristics about the maps, we can create a more accurate heuristic for IDA* to improve it's performance.

My conclusion is that IDA* will only work better with smaller inputs and with situations where the heuristic works best. These findings are in line with my source materials, as they implied that IDA*'s time efficiency relies heavily on the heuristic.

## Flaws and possible improvements

Algorithm functions could be improved if the map is initialized before the algorthm functions are called. I decided that I will add the initialization time with the actual algorithm's run time, because the map still needs to be processed to a correct form (graph, matrix, etc), so technically it is part of the algorithm. If I was to make a perfectly optimized program, this would be my only improvement on performance.

The program could be prettier, but looks weren't the focus, so I don't mind a boring gui.

## Sources

Tirakirja by Antti Laaksonen [https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/]

IDA* Algorithm in general by algorithmsinsight [https://algorithmsinsight.wordpress.com/graph-theory-2/ida-star-algorithm-in-general/]

Iterative deepening A* - Wikipedia [https://en.wikipedia.org/wiki/Iterative_deepening_A*]

Time complexity of iterative-deepening-A by R. Korf, M. Reid, S. Edelkamp 2001 [https://doi.org/10.1016/S0004-3702(01)00094-7]