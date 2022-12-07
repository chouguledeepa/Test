from resources.base import ResourceBase
from utils.fetch_data import fetch_data


class Vehicles(ResourceBase):
    """
    Resource class plural
    """

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/vehicles/"  # plural
        self.__vehicles_range = [1, 39]

    @property
    def range(self):
        return self.__vehicles_range

    @range.setter
    def range(self, new_range):
        self.__vehicles_range = new_range

    def get_count(self):
        plural_vehicles_url = self.home_url+self.__relative_url
        response = fetch_data(plural_vehicles_url)
        return response.get("count")

    def get_resource_urls(self):
        resource_url = self.home_url + self.__relative_url
        return resource_url
