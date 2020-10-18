import tkinter as tk
from src.view.smiley import Smiley


class Header:
    def __init__(self, parent, smiley_callback):
        self.smiley_callback = smiley_callback

        self.main_frame = tk.Frame(parent, height=48, width=250)
        self.main_frame.grid(row=1, padx=10, pady=1)
        self.main_frame.grid_propagate(0)
        self.main_frame['relief'] = tk.SUNKEN
        self.main_frame["borderwidth"] = 5

        self.mines_left_frame = tk.Frame(self.main_frame, height=21, width=80)
        self.mines_left_frame.grid(row=0, column=0)
        self.mines_left_frame.grid_propagate(0)
        self.mines_left_label = tk.Label(self.mines_left_frame)
        self.mines_left_label.grid(padx=10)

        self.smiley = Smiley(self.main_frame, self.smiley_callback)

        self.time_frame = tk.Frame(self.main_frame)
        self.time_frame.grid(row=0, column=5)
        self.time_label = tk.Label(self.time_frame)
        self.time_label.grid(padx=30)

    def set_time(self, time):
        self.time_label["text"] = "{}".format(str(time))

    def set_mines_left(self, mines_left):
        self.mines_left_label['text'] = "Mines : {}".format(str(mines_left))

    def set_smiley_face(self):
        self.smiley.set_smiley_face()

    def set_sunglasses_face(self):
        self.smiley.set_sunglasses_face()

    def set_dead_face(self):
        self.smiley.set_dead_face()
