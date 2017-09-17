import tkinter as tk
from enum import Enum


class ButtonState(Enum):
    NORMAL = 0
    FLAGGED = 1
    QUESTION_MARK = 2


class TileButton(tk.Button):
    def __init__(self, parent, i, j, left_click_callback, right_click_callback):
        super().__init__(parent, command=self.on_left_click, text="    ")
        self.grid(row=i, column=j)
        self["relief"] = tk.RAISED
        self["borderwidth"] = 3
        self.grid_propagate(0)

        self.i = i
        self.j = j
        self.left_click_callback = left_click_callback
        self.right_click_callback = right_click_callback
        self.state = ButtonState.NORMAL
        self.bind("<Button-3>", self.on_right_click)
    
    def on_left_click(self):
        self.destroy()
        self.left_click_callback(self.i, self.j)
        
    def on_right_click(self, _):
        if self.state == ButtonState.NORMAL:
            self["text"] = "  ! "
            self["foreground"] = "red"
            self.state = ButtonState.FLAGGED
        elif self.state == ButtonState.FLAGGED:
            self["text"] = " ? "
            self["foreground"] = "black"
            self.state = ButtonState.QUESTION_MARK
        elif self.state == ButtonState.QUESTION_MARK:
            self["text"] = "    "
            self.state = ButtonState.NORMAL
        self.right_click_callback(self.i, self.j, self.state)
