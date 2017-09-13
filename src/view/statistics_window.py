import tkinter as tk
from view.window import Window

class StatisticsWindow(Window):
    def __init__(self, games, wins, highscore):
        super().__init__("statistics")
        tableFrame = tk.Frame(self.window, height = 30, width = 30)
        tableFrame.grid(row=1, pady=1)
        tableFrame['relief']=tk.SUNKEN
        tableFrame["borderwidth"]=5
        
        # TODO: clean this up !
        tk.Label(tableFrame, text="Difficulty").grid(row=1,column=1,padx=5,pady=2)
        tk.Label(tableFrame, text="Easy").grid(row=1,column=2,padx=5,pady=2)
        tk.Label(tableFrame, text="Medium").grid(row=1,column=3,padx=5,pady=2)
        tk.Label(tableFrame, text="Hard").grid(row=1,column=4,padx=5,pady=2)
        tk.Label(tableFrame, text="Game Started").grid(row=2,column=1,padx=5,pady=2)
        tk.Label(tableFrame, text=str(games)).grid(row=2,column=2,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=2,column=3,padx=5,pady=5)
        tk.Label(tableFrame, text="N/A").grid(row=2,column=4,padx=5,pady=2)
        tk.Label(tableFrame, text="Game Won").grid(row=3,column=1,padx=5,pady=2)
        tk.Label(tableFrame, text=str(wins)).grid(row=3,column=2,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=3,column=3,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=3,column=4,padx=5,pady=2)
        tk.Label(tableFrame, text="% Game Won").grid(row=4,column=1,padx=5,pady=2)
        tk.Label(tableFrame, text=str(int(100*wins/games))+"%").grid(row=4,column=2,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=4,column=3,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=4,column=4,padx=5,pady=2)
        tk.Label(tableFrame, text="Best Time").grid(row=5, column=1,padx=5,pady=2)
        tk.Label(tableFrame, text=str(highscore)).grid(row=5,column=2,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=5,column=3,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=5,column=4,padx=5,pady=2)

        close = tk.Button(self.window, command=self.window.destroy, text="close")
        close.grid(row=2, padx=100, pady=25)