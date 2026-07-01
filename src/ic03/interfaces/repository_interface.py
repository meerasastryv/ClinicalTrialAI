from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    """
    Interface for repositories.
    """

    @abstractmethod
    def save(self, obj):
        pass

    @abstractmethod
    def get_all(self):
        pass
