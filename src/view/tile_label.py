import tkinter as tk


class TileLabel(tk.Label):
    colors = ["blue", "blue", "forest green", "orange red", "navy", "brown", "light sea green", "black", "gray",
              "black"]
    texts = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "x"]
    
    def __init__(self, parent, i, j, number, callback):
        super().__init__(parent, text=TileLabel.texts[number], fg=TileLabel.colors[number])
        self.grid(row=i, column=j, padx=8, pady=6)
        self.callback = callback
        self.row = i
        self.column = j
        self.number = number
        self.bind("<Button-1>", self.on_left_click)
        
    def on_left_click(self, _):
        self.callback(self.row, self.column)
