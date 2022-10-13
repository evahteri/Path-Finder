import os
from tkinter import constants, ttk, Canvas, StringVar
from algorithms.ida_star import IdaStar
from algorithms.dijkstra import Dijkstra


class StartViewUi:
    """Class responsible for start view

    """

    def __init__(self, root):
        self._root = root
        self._frame = None
        self.grid = Canvas(self._root, width=500, height=500)
        self.start_coordinate = None
        self.end_coordinate = None
        self.current_map = None
        self._pixel_size = None
        self.map_size = 0
        self.maps = []

        self._base()

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

        start_coordinate_header = ttk.Label(
            master=self._frame, text="Select start coordinate (for example: (0,0))")
        self.start_coordinate_entry = ttk.Entry(
            master=self._frame, textvariable=self.start_coordinate)

        start_coordinate_header.grid(row=0, column=0)
        self.start_coordinate_entry.grid(row=0, column=1)

        end_coordinate_header = ttk.Label(
            master=self._frame, text="Select end coordinate (for example: (9,9))")
        self.end_coordinate_entry = ttk.Entry(
            master=self._frame, textvariable=self.end_coordinate)

        end_coordinate_header.grid(row=2, column=0)
        self.end_coordinate_entry.grid(row=2, column=1)

        map_header = ttk.Label(master=self._frame, text="Select map")
        for file in os.listdir("src/static/maps"):
            self.maps.append(file)
        map_header.grid(row=4, column=0)

        self.current_map = StringVar(master=self._frame)
        map_selection = ttk.OptionMenu(self._frame, self.current_map, self.maps[0], *self.maps)
        map_selection.grid(row=5, column=0)

        algo_header = ttk.Label(master=self._frame, text="Select algorithm")
        algo_header.grid(row=7, column=0)

        ida_star_button = ttk.Button(
            master=self._frame, text="IDA*", command=self._handle_ida_star
        )
        ida_star_button.grid(row=8, column=0)

        dijkstra_button = ttk.Button(
            master=self._frame, text="Dijkstra", command=self._handle_dijkstra
        )
        show_map_button = ttk.Button(
            master=self._frame, text="Show map", command=self._grid
        )
        dijkstra_button.grid(row=9, column=0)
        show_map_button.grid(row=10, column=0)
        
    def _get_map_size(self):
        size = 0
        map = self.current_map.get()
        with open(f"src/static/maps/{map}") as current_map:
            for row in current_map:
                size += 1
        return size

    def _grid(self):
        self.grid.delete("all")
        map = self.current_map.get()
        self.map_size= self._get_map_size()
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
        start = self.start_coordinate_entry.get()
        end = self.end_coordinate_entry.get()
        distance_matrix = Dijkstra(self.current_map.get()).find_route(start=start, end=end)[0]
        if distance_matrix == "incorrect input":
            return print("incorrect input")
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
        start = self.start_coordinate_entry.get()
        goal = self.end_coordinate_entry.get()
        distance_matrix = IdaStar().find_route(start=start, goal=goal)[0]
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
