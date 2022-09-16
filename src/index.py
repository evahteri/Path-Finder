from tkinter import Tk
from ui.ui import UI


def main():
    """Function that launches graphical user interface

    """
    window = Tk()
    window.title("Path Finder")

    ui_window = UI(window)
    ui_window.start()

    window.mainloop()


if __name__ == "__main__":
    main()
