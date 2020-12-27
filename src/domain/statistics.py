import math

from src.domain.difficulty import Difficulty


class DifficultyStatistics:
    def __init__(self, games_started=0, games_won=0, best_time=math.inf):
        self.games_started = games_started
        self.games_won = games_won
        self.best_time = best_time

    def __eq__(self, other):
        if not isinstance(other, DifficultyStatistics):
            return False

        return (self.games_started == other.games_started and
                self.games_won == other.games_won and
                self.best_time == other.best_time)

    def __ne__(self, other):
        return not self.__eq__(other)


class Statistics:
    def __init__(self):
        self._stats = Statistics._create_empty()

    @staticmethod
    def _create_empty():
        stats = {
            Difficulty.EASY: DifficultyStatistics(),
            Difficulty.MEDIUM: DifficultyStatistics(),
            Difficulty.HARD: DifficultyStatistics()
        }
        return stats

    def reset(self):
        self._stats = Statistics._create_empty()

    def get_games_started(self, difficulty: Difficulty):
        return self._stats[difficulty].games_started

    def increment_games_started(self, difficulty: Difficulty):
        self._stats[difficulty].games_started += 1

    def get_games_won(self, difficulty: Difficulty):
        return self._stats[difficulty].games_won

    def increment_games_won(self, difficulty: Difficulty):
        self._stats[difficulty].games_won += 1

    def get_win_rate(self, difficulty: Difficulty):
        if self._stats[difficulty].games_started == 0:
            return 0

        return int(100 * self._stats[difficulty].games_won / self._stats[difficulty].games_started)

    def get_best_time(self, difficulty: Difficulty):
        return self._stats[difficulty].best_time

    def set_best_time(self, difficulty: Difficulty, time):
        self._stats[difficulty].best_time = time

    def is_best_time(self, difficulty: Difficulty, time):
        return time < self._stats[difficulty].best_time

    def __eq__(self, other):
        if not isinstance(other, Statistics):
            return False

        return self._stats == other._stats

    def __ne__(self, other):
        return not self.__eq__(other)
