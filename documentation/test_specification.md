# Testing

## Automatic testing

Testing is done with pytest and currently tests if Dijkstra and IDA* finds fastest route through the map. First, Dijkstra is tested with manually counted shortest paths, with different inputs. Now we can be sure that Dijkstra always finds the correct route. IDA* is tested with the help of Dijkstra; every output has to mach Dijkstra's output to make sure the route is correct.

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

There are no automated performance tests. The program prints time spent getting the result to the terminal so user can inspect and compare these numbers together.