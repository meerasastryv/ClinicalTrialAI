from abc import ABC, abstractmethod


class ServiceInterface(ABC):
    """
    Interface for services.
    """

    @abstractmethod
    def execute(self):
        pass
