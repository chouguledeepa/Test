from resources.base import ResourceBase
from utils.fetch_data import fetch_data


class Species(ResourceBase):
    """
    Resource class plural
    """

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/species/"  # plural
        self.__species_range = [1, 37]

    @property
    def range(self):
        return self.__species_range

    @range.setter
    def range(self, new_range):
        self.__species_range = new_range

    def get_count(self):
        plural_species_url = self.home_url+self.__relative_url
        response = fetch_data(plural_species_url)
        return response.get("count")

    def get_resource_urls(self):
        resource_url = self.home_url + self.__relative_url
        return resource_url

# s = Species()
# print(s.range)
# s.range = [2,5]
# print(s.range)