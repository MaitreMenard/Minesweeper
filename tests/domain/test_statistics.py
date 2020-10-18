import unittest

from src.domain.difficulty import Difficulty
from src.domain.statistics import Statistics


class StatisticsTest(unittest.TestCase):
    DIFFICULTY = Difficulty.EASY
    OLD_BEST_TIME = 30

    def setUp(self):
        self.statistics = Statistics()

    def test_increment_games_started(self):
        initial_games_started = self.statistics.get_games_started(self.DIFFICULTY)

        self.statistics.increment_games_started(self.DIFFICULTY)

        final_games_started = self.statistics.get_games_started(self.DIFFICULTY)
        self.assertEqual(final_games_started, initial_games_started + 1)

    def test_increment_games_won(self):
        initial_games_won = self.statistics.get_games_won(self.DIFFICULTY)

        self.statistics.increment_games_won(self.DIFFICULTY)

        final_games_won = self.statistics.get_games_won(self.DIFFICULTY)
        self.assertEqual(final_games_won, initial_games_won + 1)

    def test_get_win_rate(self):
        self.statistics.increment_games_won(self.DIFFICULTY)
        for _ in range(4):
            self.statistics.increment_games_started(self.DIFFICULTY)

        win_rate = self.statistics.get_win_rate(self.DIFFICULTY)

        self.assertEqual(win_rate, 25)

    def test_initial_win_rate(self):
        win_rate = self.statistics.get_win_rate(self.DIFFICULTY)

        self.assertEqual(win_rate, 0)

    def test_is_best_time_should_return_true_when_faster_than_best_time(self):
        self.statistics.set_best_time(self.DIFFICULTY, self.OLD_BEST_TIME)

        is_best_time = self.statistics.is_best_time(self.DIFFICULTY, self.OLD_BEST_TIME - 1)

        self.assertTrue(is_best_time)

    def test_is_best_time_should_return_false_when_slower_than_best_time(self):
        self.statistics.set_best_time(self.DIFFICULTY, self.OLD_BEST_TIME)

        is_best_time = self.statistics.is_best_time(self.DIFFICULTY, self.OLD_BEST_TIME + 1)

        self.assertFalse(is_best_time)
