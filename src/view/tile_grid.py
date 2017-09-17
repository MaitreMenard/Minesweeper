import tkinter as tk

from view.tile_label import TileLabel
from view.tile_button import TileButton


class TileGrid:
    def __init__(self, parent, minefield, left_click_callback, right_click_callback, label_callback):
        self.height = minefield.height
        self.width = minefield.width
        self.button_list = []
        self.frame = tk.Frame(parent, height=347, width=277)
        self.frame.grid(padx=6, pady=4)
        self.frame['relief'] = tk.SUNKEN
        self.frame["borderwidth"] = 5
        self.frame.grid_propagate(0)

        for i in range(self.height):
            row = []
            for j in range(self.width):
                if minefield.has_mine_at_position(i, j):
                    TileLabel(self.frame, i, j, -1, label_callback)
                else:
                    TileLabel(self.frame, i, j, minefield[i, j].adjacent_mines, label_callback)
                row.append(TileButton(self.frame, i, j, left_click_callback, right_click_callback))

            self.button_list.append(row)

    def destroy(self):
        if len(self.button_list) != 0:
            for i in range(self.height):
                for j in range(self.width):
                    self.button_list[i][j].destroy()
            self.button_list.clear()
        self.frame.destroy()

    def reveal_tile(self, i, j):
        self.button_list[i][j].on_left_click()
