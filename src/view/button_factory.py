import tkinter as tk

from view.tile_button import TileButton


class ButtonFactory:
    def __init__(self, left_click_callback, right_click_callback):
        self.left_click_callback = left_click_callback
        self.right_click_callback = right_click_callback
        self.default_image = tk.PhotoImage(file="resources/button_default(small).gif")
        self.flagged_image = tk.PhotoImage(file="resources/button_flagged(small).gif")
        self.question_mark_image = tk.PhotoImage(file="resources/button_question_mark(small).gif")

    def create(self, button_parent, i, j):
        return TileButton(button_parent, i, j, self.left_click_callback, self.right_click_callback, self.default_image,
                          self.flagged_image, self.question_mark_image)
