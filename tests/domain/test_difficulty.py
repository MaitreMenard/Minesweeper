from unittest import TestCase

from src.domain.difficulty import Difficulty, select_configuration


class DifficultyTest(TestCase):

    def test_select_configuration_easy(self):
        config = select_configuration(Difficulty.EASY)

        self.assertEqual(config.width, 9)
        self.assertEqual(config.height, 9)
        self.assertEqual(config.mines, 10)

    def test_select_configuration_medium(self):
        config = select_configuration(Difficulty.MEDIUM)

        self.assertEqual(config.width, 16)
        self.assertEqual(config.height, 16)
        self.assertEqual(config.mines, 40)

    def test_select_configuration_hard(self):
        config = select_configuration(Difficulty.HARD)

        self.assertEqual(config.width, 30)
        self.assertEqual(config.height, 16)
        self.assertEqual(config.mines, 99)
