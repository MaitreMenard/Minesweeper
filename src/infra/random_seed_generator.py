import random

from src.domain.seed_generator import SeedGenerator


class RandomSeedGenerator(SeedGenerator):

    def generate(self) -> int:
        return random.randrange(10000)
