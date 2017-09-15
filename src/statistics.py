import math
from difficulty import Difficulty


class Statistics:
    def __init__(self):
        self._stats = Statistics._create_empty()
        self.load()

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
    
    def load(self):
        file = open("stats.txt", "r")
        lines = file.readlines()
        file.close()
        print(lines)
        self._stats[Difficulty.EASY]["best time"] = int(lines[0])
        self._stats[Difficulty.EASY]["games started"] = int(lines[1])
        self._stats[Difficulty.EASY]["games won"] = int(lines[2])
    
    def save(self):
        file = open("stats.txt", "w")
        file.write(str(self._stats[Difficulty.EASY]["games started"]) + "\n")
        file.write(str(self._stats[Difficulty.EASY]["games won"]) + "\n")
        file.write(str(self._stats[Difficulty.EASY]["best time"]))
        file.close()
    
    def reset(self):
        self._stats = Statistics._create_empty()
        self.save()

    def increment_games_started(self, difficulty):
        self._stats[difficulty]["games started"] += 1

    def increment_games_won(self, difficulty):
        self._stats[difficulty]["games won"] += 1

    def set_best_time(self, difficulty, score):
        self._stats[difficulty]["best time"] = score
