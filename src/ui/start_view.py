from tkinter import constants, ttk, Canvas
from PIL import Image, ImageTk


class StartViewUi:
    """Class responsible for start view

    """
    def __init__(self, root):
        self._root = root
        self._frame = None

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

        header = ttk.Label(master=self._frame, text="Select algorithm")
        header.grid(row=0, column=0)

        ida_star_button = ttk.Button(
            master=self._frame, text="IDA*", command=None
        )
        ida_star_button.grid(row=2, column=0)

        dijkstra_button = ttk.Button(
            master=self._frame, text="Dijkstra", command=None
        )
        dijkstra_button.grid(row=3, column=0)

    def _grid(self):
        size = 20
        grid = Canvas(self._root)

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
                    grid.create_rectangle((x1, y1, x2, y2), fill=color)
                    x += 1
        grid.pack()
