# Testing

## Automatic testing

Testing is done with pytest and currently tests if Dijkstra and IDA* finds fastest route through the map. They find paths differently so the right output in both test cases is different. Both tests are done with same input ((0,0) and (9,9)), from left upper corner to the lower right corner). Tests can be run with command

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

Routes are visualized in graphic user interface. Visited nodes (pixels) are yellow, fastest route is green and unvisited nodes stay white. Currentlty it is up to the user to decide if the result is correct by counting the fastest route manually.

## Performance testing

There are no automated performance tests. The program prints time spent getting the result to the terminal so user can inspect and compare these numbers together.