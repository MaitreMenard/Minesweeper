import tkinter as tk
from view.window import Window


class StatisticsWindow(Window):
    def __init__(self, games, wins, high_score):
        super().__init__("statistics")
        table_frame = tk.Frame(self.window, height=30, width=30)
        table_frame.grid(row=1, pady=1)
        table_frame['relief'] = tk.SUNKEN
        table_frame["borderwidth"] = 5
        
        # TODO: clean this up !
        tk.Label(table_frame, text="Difficulty").grid(row=1, column=1, padx=5, pady=2)
        tk.Label(table_frame, text="Easy").grid(row=1, column=2, padx=5, pady=2)
        tk.Label(table_frame, text="Medium").grid(row=1, column=3, padx=5, pady=2)
        tk.Label(table_frame, text="Hard").grid(row=1, column=4, padx=5, pady=2)
        tk.Label(table_frame, text="Game Started").grid(row=2, column=1, padx=5, pady=2)
        tk.Label(table_frame, text=str(games)).grid(row=2, column=2, padx=5, pady=2)
        tk.Label(table_frame, text="N/A").grid(row=2, column=3, padx=5, pady=5)
        tk.Label(table_frame, text="N/A").grid(row=2, column=4, padx=5, pady=2)
        tk.Label(table_frame, text="Game Won").grid(row=3, column=1, padx=5, pady=2)
        tk.Label(table_frame, text=str(wins)).grid(row=3, column=2, padx=5, pady=2)
        tk.Label(table_frame, text="N/A").grid(row=3, column=3, padx=5, pady=2)
        tk.Label(table_frame, text="N/A").grid(row=3, column=4, padx=5, pady=2)
        tk.Label(table_frame, text="% Game Won").grid(row=4, column=1, padx=5, pady=2)
        tk.Label(table_frame, text=str(int(100*wins/games))+"%").grid(row=4, column=2, padx=5, pady=2)
        tk.Label(table_frame, text="N/A").grid(row=4, column=3, padx=5, pady=2)
        tk.Label(table_frame, text="N/A").grid(row=4, column=4, padx=5, pady=2)
        tk.Label(table_frame, text="Best Time").grid(row=5, column=1, padx=5, pady=2)
        tk.Label(table_frame, text=str(high_score)).grid(row=5, column=2, padx=5, pady=2)
        tk.Label(table_frame, text="N/A").grid(row=5, column=3, padx=5, pady=2)
        tk.Label(table_frame, text="N/A").grid(row=5, column=4, padx=5, pady=2)

        close = tk.Button(self.window, command=self.window.destroy, text="close")
        close.grid(row=2, padx=100, pady=25)
