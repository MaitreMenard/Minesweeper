import math

from domain.difficulty import Difficulty


class Statistics:
    def __init__(self):
        self._stats = Statistics._create_empty()

    @staticmethod
    def _create_empty():
        stats = {
            Difficulty.EASY: {
                "games started": 0,
                "games won": 0,
                "best time": math.inf
            },
            Difficulty.MEDIUM: {
                "games started": 0,
                "games won": 0,
                "best time": math.inf
            },
            Difficulty.HARD: {
                "games started": 0,
                "games won": 0,
                "best time": math.inf
            }
        }
        return stats
    
    def reset(self):
        self._stats = Statistics._create_empty()

    def get_games_started(self, difficulty: Difficulty):
        return self._stats[difficulty]["games started"]

    def increment_games_started(self, difficulty: Difficulty):
        self._stats[difficulty]["games started"] += 1

    def get_games_won(self, difficulty: Difficulty):
        return self._stats[difficulty]["games won"]

    def increment_games_won(self, difficulty: Difficulty):
        self._stats[difficulty]["games won"] += 1

    def get_win_rate(self, difficulty: Difficulty):
        return int(100 * self._stats[difficulty]["games won"] / self._stats[difficulty]["games started"])

    def get_best_time(self, difficulty: Difficulty):
        return self._stats[difficulty]["best time"]

    def set_best_time(self, difficulty: Difficulty, score):
        self._stats[difficulty]["best time"] = score
