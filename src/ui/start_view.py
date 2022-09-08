from tkinter import constants, ttk
from PIL import Image, ImageTk


class StartViewUi:
    """Class responsible for start view

    """
    def __init__(self, root):
        self._root = root
        self._frame = None

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
            master=self._frame, text="Dijkstra", command=None
        )
        dijkstra_button.grid(row=3, column=0)

        map_image = Image.open("../Path_Finder/src/static/maps/berlin/berlin_256.png").resize((400,400))
        map_photo = ImageTk.PhotoImage(map_image)

        image_label = ttk.Label(master=self._frame, image=map_photo, width=256)
        image_label.image = map_photo
        image_label.grid(row=4, column=1)

