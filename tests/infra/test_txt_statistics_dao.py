import os
import unittest

from src.domain.difficulty import Difficulty
from src.domain.statistics import Statistics, DifficultyStatistics
from src.infra.txt_statistics_dao import TxtStatisticsDao


class TxtStatisticsDaoTest(unittest.TestCase):
    TEST_FILE = "tests/tmp.txt"

    def setUp(self):
        self.statistics_dao = TxtStatisticsDao(self.TEST_FILE)

        self.statistics = Statistics()
        self.statistics._stats[Difficulty.EASY] = DifficultyStatistics(1, 2, 3)
        self.statistics._stats[Difficulty.MEDIUM] = DifficultyStatistics(4, 5, 6)

    def test_save_load(self):
        self.statistics_dao.save(self.statistics)

        loaded_statistics = self.statistics_dao.load()

        self.assertEqual(self.statistics._stats, loaded_statistics._stats)

    def tearDown(self):
        os.remove(self.TEST_FILE)
