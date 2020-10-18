import math

from src.domain.difficulty import Difficulty
from src.domain.statistics import Statistics, DifficultyStatistics
from src.domain.statistics_dao import StatisticsDao


class TxtStatisticsDao(StatisticsDao):
    def __init__(self, save_filename):
        self.save_filename = save_filename

    def load(self) -> Statistics:
        file = open(self.save_filename, "r")
        lines = file.read().splitlines()
        file.close()
        print(lines)

        statistics = Statistics()
        statistics._stats[Difficulty.EASY] = self.parse_difficulty_statistics(lines, 0)
        statistics._stats[Difficulty.MEDIUM] = self.parse_difficulty_statistics(lines, 4)
        statistics._stats[Difficulty.HARD] = self.parse_difficulty_statistics(lines, 8)

        return statistics

    def save(self, statistics: Statistics) -> None:
        file = open(self.save_filename, "w")
        self.write_difficulty(file, statistics._stats[Difficulty.EASY])
        self.write_difficulty(file, statistics._stats[Difficulty.MEDIUM])
        self.write_difficulty(file, statistics._stats[Difficulty.HARD])
        file.close()

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
