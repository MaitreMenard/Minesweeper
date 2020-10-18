import abc

from src.domain.statistics import Statistics


class StatisticsDao:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self) -> Statistics:
        pass

    @abc.abstractmethod
    def save(self, statistics: Statistics) -> None:
        pass
