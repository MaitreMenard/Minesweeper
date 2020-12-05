from enum import Enum


class Difficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2


class DifficultyConfig:

    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines


def select_configuration(difficulty: Difficulty) -> DifficultyConfig:
    if difficulty == Difficulty.EASY:
        return DifficultyConfig(9, 9, 10)
    elif difficulty == Difficulty.MEDIUM:
        return DifficultyConfig(16, 16, 40)
    else:
        return DifficultyConfig(30, 16, 99)
