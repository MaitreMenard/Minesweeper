import math
import tkinter as tk

from src.domain.difficulty import Difficulty
from src.domain.statistics import Statistics
from src.view.menu_window import MenuWindow


class StatisticsWindow(MenuWindow):
    def __init__(self, root, statistics: Statistics):
        super().__init__(root, "statistics")
        table_frame = tk.Frame(self.window, height=30, width=30)
        table_frame.grid(row=1, pady=1)
        table_frame['relief'] = tk.SUNKEN
        table_frame["borderwidth"] = 5

        tk.Label(table_frame, text="Difficulty").grid(row=1, column=1, padx=5, pady=2)
        tk.Label(table_frame, text="Easy").grid(row=1, column=2, padx=5, pady=2)
        tk.Label(table_frame, text="Medium").grid(row=1, column=3, padx=5, pady=2)
        tk.Label(table_frame, text="Hard").grid(row=1, column=4, padx=5, pady=2)

        tk.Label(table_frame, text="Games Started").grid(row=2, column=1, padx=5, pady=2)
        tk.Label(table_frame, text=str(statistics.get_games_started(Difficulty.EASY))).grid(row=2, column=2, padx=5,
                                                                                            pady=2)
        tk.Label(table_frame, text=str(statistics.get_games_started(Difficulty.MEDIUM))).grid(row=2, column=3, padx=5,
                                                                                              pady=5)
        tk.Label(table_frame, text=str(statistics.get_games_started(Difficulty.HARD))).grid(row=2, column=4, padx=5,
                                                                                            pady=2)

        tk.Label(table_frame, text="Games Won").grid(row=3, column=1, padx=5, pady=2)
        tk.Label(table_frame, text=str(statistics.get_games_won(Difficulty.EASY))).grid(row=3, column=2, padx=5, pady=2)
        tk.Label(table_frame, text=str(statistics.get_games_won(Difficulty.MEDIUM))).grid(row=3, column=3, padx=5,
                                                                                          pady=2)
        tk.Label(table_frame, text=str(statistics.get_games_won(Difficulty.HARD))).grid(row=3, column=4, padx=5, pady=2)

        tk.Label(table_frame, text="Win Rate").grid(row=4, column=1, padx=5, pady=2)
        tk.Label(table_frame, text=self.format_win_rate(statistics, Difficulty.EASY)).grid(row=4, column=2, padx=5,
                                                                                           pady=2)
        tk.Label(table_frame, text=self.format_win_rate(statistics, Difficulty.MEDIUM)).grid(row=4, column=3, padx=5,
                                                                                             pady=2)
        tk.Label(table_frame, text=self.format_win_rate(statistics, Difficulty.HARD)).grid(row=4, column=4, padx=5,
                                                                                           pady=2)

        tk.Label(table_frame, text="Best Time").grid(row=5, column=1, padx=5, pady=2)
        tk.Label(table_frame, text=self.format_best_time(statistics, Difficulty.EASY)).grid(row=5, column=2, padx=5,
                                                                                            pady=2)
        tk.Label(table_frame, text=self.format_best_time(statistics, Difficulty.MEDIUM)).grid(row=5, column=3, padx=5,
                                                                                              pady=2)
        tk.Label(table_frame, text=self.format_best_time(statistics, Difficulty.HARD)).grid(row=5, column=4, padx=5,
                                                                                            pady=2)

        close = tk.Button(self.window, command=self.window.destroy, text="close")
        close.grid(row=2, padx=100, pady=25)

    @staticmethod
    def format_win_rate(statistics: Statistics, difficulty: Difficulty):
        return str(statistics.get_win_rate(difficulty)) + "%"

    @staticmethod
    def format_best_time(statistics: Statistics, difficulty: Difficulty):
        best_time = statistics.get_best_time(difficulty)

        if best_time == math.inf:
            return "N/A"
        else:
            return str(best_time)
