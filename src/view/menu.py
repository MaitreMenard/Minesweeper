import tkinter as tk


class Menu:
    def __init__(self, root, new_game_callback, statistics_callback, options_callback, exit_callback):
        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=0)
        self.menu_button = tk.Menubutton(self.frame, anchor=tk.W, text="Game")
        self.menu_button.grid(row=0, column=0)
        self.menu_button.menu = tk.Menu(self.menu_button, tearoff=0)
        self.menu_button["menu"] = self.menu_button.menu
        self.menu_button.menu.add_command(command=new_game_callback, label="New Game")
        self.menu_button.menu.add_command(command=statistics_callback, label="Statistics")
        self.menu_button.menu.add_command(command=options_callback, label="Options")
        self.menu_button.menu.add_command(command=exit_callback, label="Exit")
