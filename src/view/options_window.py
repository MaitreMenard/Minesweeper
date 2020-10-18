import tkinter as tk
from src.view.menu_window import MenuWindow


class OptionsWindow(MenuWindow):
    def __init__(self, root):
        super().__init__(root, "options")
        close = tk.Button(self.window, command=self.window.destroy, text="close")
        close.grid(padx=100, pady=50)
