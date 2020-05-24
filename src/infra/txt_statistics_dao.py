from domain.difficulty import Difficulty
from domain.statistics import Statistics
from domain.statistics_dao import StatisticsDao


class TxtStatisticsDao(StatisticsDao):
    SAVE_FILENAME = "infra/stats.txt"

    def load(self) -> Statistics:
        file = open(self.SAVE_FILENAME, "r")
        lines = file.readlines()
        file.close()
        print(lines)

        statistics = Statistics()
        statistics._stats[Difficulty.EASY]["best time"] = int(lines[0])
        statistics._stats[Difficulty.EASY]["games started"] = int(lines[1])
        statistics._stats[Difficulty.EASY]["games won"] = int(lines[2])

        return statistics

    def save(self, statistics: Statistics) -> None:
        file = open(self.SAVE_FILENAME, "w")
        file.write(str(statistics._stats[Difficulty.EASY]["best time"]) + "\n")
        file.write(str(statistics._stats[Difficulty.EASY]["games started"]) + "\n")
        file.write(str(statistics._stats[Difficulty.EASY]["games won"]))
        file.close()
