# User guide

This program is for finding shortest routes through a map and comparing two path-finding algorithms, IDA* and Dijkstra.

## Installing the program

Run this command inside the folder

```bash
poetry install
```

## Launching the program

Launch the program by running 

```bash
poetry run invoke start
```
in the folder.

This view should pop up:

![start view](https://github.com/evahteri/Path-Finder/blob/main/documentation/start_view.png)

## Using the program

On the top you can see current selected map. You can select the map from "Select map" button. Once selected, press "Show map" to see it. All maps are in src/static/maps folder. If you'd like to use your own maps, create a text file in that folder. Note that length and height should be the same. Please do not change the maps' names to ensure that there are no errors during performance tests/automated tests.

You can search shortest paths by entering coordinates to the text fields. Only numbers are accepted as input. Note that the left upper corner is (0,0). The program will notify is the input is incorrect. After you have entered the coordinates, press either Dijkstra or IDA* to find the route. The run time and path distance are printed to terminal. Shortest route is marked as green tiles in the map. Visited tiles are yellow and the start and goal nodes are violet.

From the start view, you can also run performance tests. Results are shown both in a messagebox and in terminal. You can also run performance tests using current map and the program will plot the results.

Program can be closed by closing the window.