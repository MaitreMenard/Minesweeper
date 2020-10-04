import tkinter as tk


class TileLabel(tk.Frame):
    COLORS = ["blue", "blue", "forest green", "orange red", "navy", "brown", "light sea green", "black", "gray",
              "black"]
    TEXTS = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "x"]
    
    def __init__(self, parent, i, j, number, callback):
        super().__init__(parent, height=36, width=36)
        self.pack_propagate(0)
        self.grid(row=i, column=j)

        self.label = tk.Label(self, text=TileLabel.TEXTS[number], fg=TileLabel.COLORS[number])
        self.label.bind("<Button-1>", self.on_left_click)
        self.label.pack(fill=tk.BOTH, expand=1)

        self.callback = callback
        self.row = i
        self.column = j
        self.number = number

    def on_left_click(self, _):
        self.callback(self.row, self.column)
