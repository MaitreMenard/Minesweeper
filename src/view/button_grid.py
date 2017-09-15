import tkinter as tk


class ButtonGrid:
    def __init__(self, parent):
        self.parent = parent
        self.cadre2 = tk.Frame(self.parent, height=347, width=277)
        self.cadre2.grid(padx=6, pady=4)
        self.cadre2['relief'] = tk.SUNKEN
        self.cadre2["borderwidth"] = 5
        self.cadre2.grid_propagate(0)
