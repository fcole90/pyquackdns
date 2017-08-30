# Library of functions interacting with DuckDNS
from abc import ABC, abstractmethod
import requests


class AbstractUpdater(ABC):
    """
    Abstract class that defines the methods
    every Updater should have.
    """

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def update(self):
        pass


class MockUpdater(AbstractUpdater):
    """
    Mock updater implementation which fakes a class
    to update the DuckDNS information.
    """

    def update(self):
        response = "Updated!"
        return response
