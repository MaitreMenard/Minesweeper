import tkinter as tk
from enum import Enum


class ButtonState(Enum):
    NORMAL = 0
    FLAGGED = 1
    QUESTION_MARK = 2


class TileButton(tk.Button):
    IMAGE_SIZE = 30
    BORDERWIDTH = 3
    TOTAL_SIZE = IMAGE_SIZE + 2 * BORDERWIDTH

    def __init__(self, parent, i, j, left_click_callback, right_click_callback, default_image, flagged_image,
                 question_mark_image):
        super().__init__(parent, command=self.on_left_click, image=default_image, height=TileButton.IMAGE_SIZE,
                         width=TileButton.IMAGE_SIZE, padx=0, pady=0, highlightthickness=0)
        self.grid(row=i, column=j)
        self["relief"] = tk.RAISED
        self["borderwidth"] = TileButton.BORDERWIDTH
        self.grid_propagate(0)

        self.i = i
        self.j = j
        self.left_click_callback = left_click_callback
        self.right_click_callback = right_click_callback
        self.default_image = default_image
        self.flagged_image = flagged_image
        self.question_mark_image = question_mark_image
        self.state = ButtonState.NORMAL
        self.bind("<Button-3>", self.on_right_click)

    def on_left_click(self):
        self.left_click_callback(self.i, self.j)

    def on_right_click(self, _):
        if self.state == ButtonState.NORMAL:
            self["image"] = self.flagged_image
            self.state = ButtonState.FLAGGED
        elif self.state == ButtonState.FLAGGED:
            self["image"] = self.question_mark_image
            self.state = ButtonState.QUESTION_MARK
        elif self.state == ButtonState.QUESTION_MARK:
            self["image"] = self.default_image
            self.state = ButtonState.NORMAL
        self.right_click_callback(self.i, self.j, self.state)
