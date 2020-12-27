import math
import os

from src.domain.difficulty import Difficulty
from src.domain.statistics import Statistics, DifficultyStatistics
from src.domain.statistics_dao import StatisticsDao


class TxtStatisticsDao(StatisticsDao):
    def __init__(self, save_filename):
        self.save_filename = save_filename

    def load(self) -> Statistics:
        statistics = Statistics()

        lines = self._read_save_file()
        if lines is not None:
            statistics._stats[Difficulty.EASY] = self.parse_difficulty_statistics(lines, 0)
            statistics._stats[Difficulty.MEDIUM] = self.parse_difficulty_statistics(lines, 4)
            statistics._stats[Difficulty.HARD] = self.parse_difficulty_statistics(lines, 8)

        return statistics

    def _read_save_file(self):
        try:
            with open(self.save_filename, "r") as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return None

    def save(self, statistics: Statistics) -> None:
        self._create_directory_if_necessary()

        with open(self.save_filename, "w") as file:
            self.write_difficulty(file, statistics._stats[Difficulty.EASY])
            self.write_difficulty(file, statistics._stats[Difficulty.MEDIUM])
            self.write_difficulty(file, statistics._stats[Difficulty.HARD])

    def _create_directory_if_necessary(self):
        os.makedirs(os.path.dirname(self.save_filename), exist_ok=True)

    @staticmethod
    def parse_difficulty_statistics(lines, first_line_index):
        return DifficultyStatistics(games_started=int(lines[first_line_index + 1]),
                                    games_won=int(lines[first_line_index + 2]),
                                    best_time=TxtStatisticsDao.parse_best_time(lines[first_line_index]))

    @staticmethod
    def parse_best_time(line):
        if line == "inf":
            return math.inf
        else:
            return int(line)

    @staticmethod
    def write_difficulty(file, difficulty_stats):
        file.write(str(difficulty_stats.best_time) + "\n")
        file.write(str(difficulty_stats.games_started) + "\n")
        file.write(str(difficulty_stats.games_won) + "\n")
        file.write("\n")
