from ui.start_view import StartViewUi


class UI:
    """Class that handles all ui elements

    """

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        """Launches the start view
        """
        self._show_start_view()

    def _show_start_view(self):
        self._current_view = StartViewUi(self._root)

        self._current_view.pack()
