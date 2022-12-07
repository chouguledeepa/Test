from abc import ABC, abstractmethod


class ResourceBase(ABC):
    """
    Base class representing required methods to be implemented by all resource
    classes
    """

    resources = ["planets", "starships", "people", "vehicles", "films", "species"]

    def __init__(self):
        self.home_url = "https://swapi.dev/"

    @abstractmethod
    def get_count(self):
        pass

    @abstractmethod
    def get_resource_urls(self):
        pass
