from tkinter import constants, ttk, Canvas
from PIL import Image, ImageTk
from algorithms.dijkstra import Dijkstra


class StartViewUi:
    """Class responsible for start view

    """
    def __init__(self, root):
        self._root = root
        self._frame = None
        self.grid = Canvas(self._root)

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

        header = ttk.Label(master=self._frame, text="Select algorithm")
        header.grid(row=0, column=0)

        ida_star_button = ttk.Button(
            master=self._frame, text="IDA*", command=None
        )
        ida_star_button.grid(row=2, column=0)

        dijkstra_button = ttk.Button(
            master=self._frame, text="Dijkstra", command=self._handle_dijkstra
        )
        show_map_button = ttk.Button(
            master=self._frame, text="Show map", command=self._grid
        )
        dijkstra_button.grid(row=3, column=0)
        show_map_button.grid(row=4, column=0)

    def _grid(self):
        size = 20

        with open("../Path_Finder/src/static/maps/map_1.txt") as map:
            y = 0
            x = 0
            for row in map:
                y += 1
                x = 0
                for coordinate in row:
                    if x == 10:
                        break
                    if coordinate == ".":
                        color = "white"
                    if coordinate == "@":
                        color = "black"
                    if coordinate == "x":
                        color = "red"
                    x1 = x*size
                    y1 = y*size
                    x2 = x1 + size
                    y2 = y1 + size
                    self.grid.create_rectangle((x1, y1, x2, y2), fill=color)
                    x += 1
        self.grid.pack()

    def _handle_dijkstra(self):
        size = 20
        distance_matrix = Dijkstra().find_route()
        x = 0
        y = 0
        for row in distance_matrix:
            y += 1
            x = 0
            for coordinate in row:
                color = "yellow"
                if x == 10:
                        break
                if coordinate == 999:
                    color = "white"
                if coordinate == "@":
                    color = "black"
                if coordinate == "x":
                    color = "green"
                x1 = x*size
                y1 = y*size
                x2 = x1 + size
                y2 = y1 + size
                self.grid.create_rectangle((x1, y1, x2, y2), fill=color)
                x += 1
        self.grid.pack()
