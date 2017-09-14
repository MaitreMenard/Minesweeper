import tkinter as tk
from view.window import Window


class OptionsWindow(Window):
    def __init__(self):
        super().__init__("options")
        close = tk.Button(self.window, command=self.window.destroy, text="close")
        close.grid(padx=100, pady=50)
