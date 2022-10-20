import os
from re import X
from tkinter import constants, ttk, Canvas, StringVar, messagebox
from algorithms.ida_star import IdaStar
from algorithms.dijkstra import Dijkstra
from performance_tests.performance import PerformanceTest
from services.map_helper import MapHelper
from services.input_check import InputCheck


class StartViewUi:
    """Class responsible for start view

    """

    def __init__(self, root):
        self._root = root
        self._frame = None
        self.grid = Canvas(self._root, width=500, height=500)
        self.start_x_coordinate = None
        self.start_y_coordinate = None
        self.end_x_coordinate = None
        self.end_y_coordinate = None
        self.current_map = None
        self._pixel_size = None
        self.map_size = 0
        self.maps = []

        self._base()
        self._grid()

    def pack(self):
        """Shows the view

        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Closes the view

        """
        self._frame.destroy()

    def _base(self):
        self._frame = ttk.Frame(master=self._root)

        # start coordinate x
        start_x_coordinate_header = ttk.Label(
            master=self._frame, text="Select x coordinate for start")
        self.start_coordinate_x_entry = ttk.Entry(
            master=self._frame, textvariable=self.start_x_coordinate, width=5)

        start_x_coordinate_header.grid(row=0, column=0)
        self.start_coordinate_x_entry.grid(row=0, column=1)

        # start coordinate y
        start_y_coordinate_header = ttk.Label(
            master=self._frame, text="Select y coordinate for start")
        self.start_coordinate_y_entry = ttk.Entry(
            master=self._frame, textvariable=self.start_y_coordinate, width=5)

        start_y_coordinate_header.grid(row=1, column=0)
        self.start_coordinate_y_entry.grid(row=1, column=1)
        # end coordinate x

        end_x_coordinate_header = ttk.Label(
            master=self._frame, text="Select x coordinate for end")
        self.end_coordinate_x_entry = ttk.Entry(
            master=self._frame, textvariable=self.end_x_coordinate, width=5)

        end_x_coordinate_header.grid(row=2, column=0)
        self.end_coordinate_x_entry.grid(row=2, column=1)

        # end coordinate y
        end_y_coordinate_header = ttk.Label(
            master=self._frame, text="Select y coordinate for end")
        self.end_coordinate_y_entry = ttk.Entry(
            master=self._frame, textvariable=self.end_y_coordinate, width=5)

        end_y_coordinate_header.grid(row=3, column=0)
        self.end_coordinate_y_entry.grid(row=3, column=1)

        map_header = ttk.Label(master=self._frame, text="Select map")
        for file in os.listdir("src/static/maps"):
            self.maps.append(file)
        map_header.grid(row=4, column=0)

        self.current_map = StringVar(master=self._frame)
        map_selection = ttk.OptionMenu(
            self._frame, self.current_map, self.maps[0], *self.maps)
        map_selection.grid(row=5, column=0)

        algo_header = ttk.Label(master=self._frame, text="Select algorithm")
        algo_header.grid(row=6, column=0)

        ida_star_button = ttk.Button(
            master=self._frame, text="IDA*", command=self._handle_ida_star
        )
        ida_star_button.grid(row=7, column=0)

        dijkstra_button = ttk.Button(
            master=self._frame, text="Dijkstra", command=self._handle_dijkstra
        )
        show_map_button = ttk.Button(
            master=self._frame, text="Show map", command=self._grid
        )
        dijkstra_button.grid(row=8, column=0)
        show_map_button.grid(row=9, column=0)

        test_performance_10x10_map_button = ttk.Button(
            master=self._frame, text="Test performance with 10X10 map", command=self._handle_performance_10x10_map
        )
        test_performance_10x10_map_button.grid(row=10, column=0)

        test_performance_15x15_map_button = ttk.Button(
            master=self._frame, text="Test performance with 15X15 map", command=self._handle_performance_15x15_map
        )
        test_performance_15x15_map_button.grid(row=11, column=0)

        test_performance_30x30_map_button = ttk.Button(
            master=self._frame, text="Test performance with 30X30 map", command=self._handle_performance_30x30_map
        )
        test_performance_30x30_map_button.grid(row=12, column=0)

        test_performance_50x50_map_button = ttk.Button(
            master=self._frame, text="Test performance with 50x50 map", command=self._handle_performance_50x50_map
        )
        test_performance_50x50_map_button.grid(row=13, column=0)

        test_performance_heap_button = ttk.Button(
            master=self._frame, text="Test heap performance with 1000 push and pop calls", command=self._handle_performance_heap
        )
        test_performance_heap_button.grid(row=15, column=0)

    def _grid(self):
        self.grid.delete("all")
        map = self.current_map.get()
        self.map_size = MapHelper(map).get_map_size()
        self._pixel_size = 300 // self.map_size
        with open(f"src/static/maps/{map}") as current_map:
            y_coordinate = 0
            x_coordinate = 0
            for row in current_map:
                y_coordinate += 1
                x_coordinate = 0
                for coordinate in row:
                    if x_coordinate == self.map_size:
                        break
                    if coordinate == ".":
                        color = "white"
                    if coordinate == "@":
                        color = "black"
                    if coordinate == "x":
                        color = "red"
                    x1 = x_coordinate*self._pixel_size
                    y1 = y_coordinate*self._pixel_size
                    x2 = x1 + self._pixel_size
                    y2 = y1 + self._pixel_size
                    self.grid.create_rectangle((x1, y1, x2, y2), fill=color)
                    x_coordinate += 1
        self.grid.pack()

    def _handle_dijkstra(self):
        self.grid.delete("all")
        start_x = self.start_coordinate_x_entry.get()
        start_y = self.start_coordinate_y_entry.get()
        end_x = self.end_coordinate_x_entry.get()
        end_y = self.end_coordinate_y_entry.get()
        if not InputCheck().check_input(current_map=self.current_map.get(), x_start=start_x, y_start=start_y, x_end=end_x, y_end=end_y):
            self._grid()
            return messagebox.showerror(title="Invalid input", message="Invalid input")
        distance_matrix = Dijkstra(self.current_map.get()).find_route(
            int(start_x), int(start_y), int(end_x), int(end_y))
        if distance_matrix:
            distance_matrix = distance_matrix[0]
        else:
            self._grid()
            return messagebox.showerror(title="No path found", message="Dijkstra could not find any path to goal node.")
        map_size = 0
        for i in distance_matrix:
            map_size += 1
        self._pixel_size = 300 // map_size
        x = 0
        y = 0
        for row in distance_matrix:
            y += 1
            x = 0
            for coordinate in row:
                color = "yellow"
                if x == map_size:
                    break
                if coordinate == "start":
                    color = "violet"
                if coordinate == "end":
                    color = "violet"
                if coordinate == 999:
                    color = "white"
                if coordinate == "@":
                    color = "black"
                if coordinate == "x":
                    color = "green"
                x1 = x*self._pixel_size
                y1 = y*self._pixel_size
                x2 = x1 + self._pixel_size
                y2 = y1 + self._pixel_size
                self.grid.create_rectangle((x1, y1, x2, y2), fill=color)
                x += 1
        self.grid.pack()

    def _handle_ida_star(self):
        self.grid.delete("all")
        start_x = self.start_coordinate_x_entry.get()
        start_y = self.start_coordinate_y_entry.get()
        end_x = self.end_coordinate_x_entry.get()
        end_y = self.end_coordinate_y_entry.get()
        if not InputCheck().check_input(current_map=self.current_map.get(), x_start=start_x, y_start=start_y, x_end=end_x, y_end=end_y):
            self._grid()
            return messagebox.showerror(title="Invalid input", message="Invalid input")
        distance_matrix = IdaStar(self.current_map.get()).find_route(
            int(start_x), int(start_y), int(end_x), int(end_y))
        if distance_matrix:
            distance_matrix = distance_matrix[0]
        else:
            self._grid()
            return messagebox.showerror(title="No path found", message="IDA* could not find any path to goal node.")
        map_size = 0
        for i in distance_matrix:
            map_size += 1
        self._pixel_size = 300 // map_size
        x = 0
        y = 0
        for row in distance_matrix:
            y += 1
            x = 0
            for coordinate in row:
                color = "yellow"
                if x == map_size:
                    break
                if coordinate == "start":
                    color = "violet"
                if coordinate == "end":
                    color = "violet"
                if coordinate == 999:
                    color = "white"
                if coordinate == "@":
                    color = "black"
                if coordinate == "x":
                    color = "green"
                x1 = x*self._pixel_size
                y1 = y*self._pixel_size
                x2 = x1 + self._pixel_size
                y2 = y1 + self._pixel_size
                self.grid.create_rectangle((x1, y1, x2, y2), fill=color)
                x += 1
        self.grid.pack()

    def _handle_performance_10x10_map(self):
        result = PerformanceTest().test_performance_10x10_map()
        return messagebox.showinfo(title="Results", message=f"100 calls made, {result[0]} was \
        {result[2]}% faster! ({result[1]} microseconds)!")
    
    def _handle_performance_15x15_map(self):
        result = PerformanceTest().test_performance_15x15_map()
        return messagebox.showinfo(title="Results", message=f"100 calls made, {result[0]} was \
        {result[2]}% faster! ({result[1]} microseconds)!")

    def _handle_performance_30x30_map(self):
        result = PerformanceTest().test_performance_30x30_map()
        return messagebox.showinfo(title="Results", message=f"100 calls made, {result[0]} was \
        {result[2]}% faster! ({result[1]} microseconds)!")

    def _handle_performance_50x50_map(self):
        result = PerformanceTest().test_performance_50x50_map()
        return messagebox.showinfo(title="Results", message=f"10 calls made, {result[0]} was \
        {result[2]}% faster! ({result[1]} microseconds)!")
    
    def _handle_performance_heap(self):
        result = PerformanceTest().test_heap_performance()
        return messagebox.showinfo(title="Results", message=f"My heap did 1000 push and pop operations in {result[0].microseconds} microseconds.\
        Python's heapq did the same in {result[1].microseconds} microseconds. ({result[2]}% faster)")
