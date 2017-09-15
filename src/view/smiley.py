import tkinter as tk


class Smiley:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback
        self.smiley_face = tk.PhotoImage(file="resources/smiley.gif").subsample(2, 2)

        self.frame = tk.Frame(self.parent)
        self.frame.grid(row=0, column=3)
        self.button = tk.Button(self.frame, image=self.smiley_face, command=self.callback, height=32, width=32)
        self.button.grid(padx=22)
