# Path Finder
Path finder is an app to find the fastest route between two locations from a map. The user can choose between two algorthms which one they want to use and gets feedback on how efficient the chosen algorithm was finding the required path.

## Algorithms
The program includes two different path finding algorithms and shows their performance differences. The first one is IDA* and the other one is Dijkstra. The program analyzes a map of a city, as a ascii grid. Each character is treated as a coordinate. Upper left corner is (0,0) and so on. Character "." is passable terrain, "@" is out of bounds.

## Time complexity

### Dijkstra
The map is analyzed as coordinates, so there are as much as nodes as coordinates. Dijkstra will go through every node and their edges, which it will perform in O(n+m) time. Dijkstra uses a heap to keep track of the unvisited and visited nodes. Heap's efficiency affects algorithm's time efficiency, but worst case scenario is O(mlogm), which happens if the algorithm has to add a node in the heap every time it handles a new edge. Total time complexity of the algorithm will be O(n+mlogm). We can expect that the map doesn't include edges that has the same start and end node. Thus m is always less than n², so time complexity improves to O(n+mlogn)

### IDA*
IDA* improves dijkstras algorithm mainly by updating a treshold, which is the maximum length of the shortest route. This is achieved by f(n) = g(n) + h(n), where g(n) is the total length from the root to node n and f(n) an estimate of the length from node n to the goal node. IDA* will stop exploring the current branch if the threshold is exceeded. Total time complexity depends how well the heuristic works, but the goal would be O(bd), where b is the branching factor and d is the shallowest depth of the tree.
## Space complexity

### Dijkstra
The algorithm keeps a long queue of nodes in memory, which can be very taxing. Worst case scenario, every node will be at some point added to the heap, so space complexity can get to O(n+m)

### IDA*
The algorithm keeps only nodes in memory that are in it's current path so the space complexity is a lot better than dijkstra's, it is O(d), where d is the shallowest goal node.


## User interface
TkInter is used as a graphic interface. There are two buttons to choose the algorithm and a search button. Future implementation would possibly include choosing freely the locations from the map. Fastest route is showed on the map as a line with the time that the result took from the algorithm.

## Programming language
I am using python and I do not know any other programming languages for peer reviewing.

## Other
My main subject/major in University of Helsinki is Tietojenkäsittelytieteiden kandidaatti. The documentation and program is in English to make sure the whole project is cohesive.

## Sources
https://en.wikipedia.org/wiki/Iterative_deepening_A*
https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/
