import abc


class SeedGenerator:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def generate(self) -> int:
        pass
