import tkinter as tk

from view.tile_button import TileButton
from view.tile_label import TileLabel


class TileGrid:
    BORDERWIDTH = 5

    def __init__(self, parent, minefield, button_factory, label_callback):
        self.height = minefield.height
        self.width = minefield.width
        self.button_list = []
        self.frame = tk.Frame(parent, height=self.size(self.height), width=self.size(self.width))
        self.frame.grid(padx=6, pady=4)
        self.frame['relief'] = tk.SUNKEN
        self.frame["borderwidth"] = TileGrid.BORDERWIDTH
        self.frame.grid_propagate(0)
        self.button_factory = button_factory

        for i in range(self.height):
            row = []
            for j in range(self.width):
                if minefield.has_mine_at_position(i, j):
                    TileLabel(self.frame, i, j, -1, label_callback)
                else:
                    TileLabel(self.frame, i, j, minefield[i, j].adjacent_mines, label_callback)
                row.append(self.button_factory.create(self.frame, i, j))

            self.button_list.append(row)

    @staticmethod
    def size(num_tiles):
        return num_tiles * TileButton.TOTAL_SIZE + 2 * TileGrid.BORDERWIDTH

    def destroy(self):
        if len(self.button_list) != 0:
            for i in range(self.height):
                for j in range(self.width):
                    self.button_list[i][j].destroy()
            self.button_list.clear()
        self.frame.destroy()

    def reveal_tile(self, i, j):
        self.button_list[i][j].on_left_click()
