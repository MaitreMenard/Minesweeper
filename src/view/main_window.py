from tkinter import Tk, PhotoImage


class MainWindow(Tk):
    ICON_FILENAME = "resources/icon.png"

    def __init__(self):
        super().__init__()
        self.title('Minesweeper')
        self.iconphoto(True, PhotoImage(file=self.ICON_FILENAME))
