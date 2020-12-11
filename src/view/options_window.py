import tkinter as tk
from src.view.menu_window import MenuWindow


class OptionsWindow(MenuWindow):
    def __init__(self, root, reset_stats_callback):
        super().__init__(root, "options")
        options_frame = tk.Frame(self.window)
        options_frame.pack(fill=tk.X, expand=1, padx=10)

        reset_stats_label = tk.Label(options_frame, text="Reset statistics", anchor="w")
        reset_stats_label.pack(fill=tk.X, expand=1, side=tk.LEFT)
        reset_stats_button = tk.Button(options_frame, command=reset_stats_callback, text="Reset")
        reset_stats_button.pack(side=tk.LEFT, pady=10)

        close = tk.Button(self.window, command=self.window.destroy, text="close")
        close.pack(padx=100, pady=25)
