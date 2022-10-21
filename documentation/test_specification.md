# Testing

## Automatic testing

Testing is done with pytest and currently tests if Dijkstra and IDA* finds fastest route through the map. First, Dijkstra is tested with manually counted shortest paths, with different inputs. Now we can be sure that Dijkstra always finds the correct route. IDA* is tested with the help of Dijkstra; every output has to match Dijkstra's output to make sure the route is correct.

```bash
poetry run invoke test
```
Current coverage report can be found [here](https://github.com/evahteri/Path-Finder/blob/main/documentation/coverage_report.png)

You can also create new coverage report by running command 

```bash
poetry run invoke coverage-report
```
This command creates a htmlcov folder, where you can find index.html. Copy it's path to your browser so you can inspect full coverage report.

## Empiric testing

Routes are visualized in graphic user interface. Visited nodes (pixels) are yellow, fastest route is green and unvisited nodes stay white. The app also prints the length of the shortest path.

## Performance testing

Both algorithms are tested with multiple inputs inside multiple maps. These tests can be run by user via gui.

Test inputs are:
- 100 random start and end coordinates inside 10x10 map
- 100 random start and end coordinates inside 15x15 map
- 100 random start and end coordinates inside 30x30 map
- 10 random start and end coordinates inside 50x50 map

There are just 10 inputs inside 50x50 map, because IDA* tends to take so much time with complicated/large maps.

Results are showed as printed lines in terminal and in a messagebox via gui. Results include run time as microseconds and percentage difference (difference in run time / slower algorithm run time * 100).

Heap's performance is tested with 1000 push and pop calls, and it is compared to Python's heapq module's heap with same calls. Function counts the time and percentage difference.

## Coverage report

![coverage report](https://github.com/evahteri/Path-Finder/blob/main/documentation/coverage_report.png)
