import tkinter as tk

from src.domain.difficulty import Difficulty


class Menu:
    def __init__(self, parent, new_game_callback, statistics_callback, options_callback, exit_callback):
        self.new_game_callback = new_game_callback
        self.frame = tk.Frame(parent)
        self.frame.grid(row=0, column=0)
        self.menu_button = tk.Menubutton(self.frame, anchor=tk.W, text="Game")
        self.menu_button.grid(row=0, column=0)
        self.menu_button.menu = tk.Menu(self.menu_button, tearoff=0)
        self.menu_button["menu"] = self.menu_button.menu
        self.create_new_game_menu(self.menu_button.menu)
        self.menu_button.menu.add_command(command=statistics_callback, label="Statistics")
        self.menu_button.menu.add_command(command=options_callback, label="Options")
        self.menu_button.menu.add_command(command=exit_callback, label="Exit")

    def create_new_game_menu(self, parent_menu: tk.Menu):
        new_game_menu = tk.Menu(parent_menu, tearoff=0)

        new_game_menu.add_command(label="Easy", command=self.easy)
        new_game_menu.add_command(label="Medium", command=self.medium)
        new_game_menu.add_command(label="Hard", command=self.hard)

        parent_menu.add_cascade(label="New Game", menu=new_game_menu)

    def easy(self):
        self.new_game_callback(Difficulty.EASY)

    def medium(self):
        self.new_game_callback(Difficulty.MEDIUM)

    def hard(self):
        self.new_game_callback(Difficulty.HARD)
