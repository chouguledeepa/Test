from resources.base import ResourceBase
from utils.fetch_data import fetch_data


class Characters(ResourceBase):
    """
    Resource class plural
    """

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/people/"  # plural
        self.__character_range = [1, 82]

    @property
    def range(self):
        return self.__character_range

    @range.setter
    def range(self, range):
        start, end = range[0], range[1]
        self.__character_range = [start, end]

    def get_count(self):
        plural_character_url = self.home_url+self.__relative_url  # plural
        response = fetch_data(plural_character_url)
        return response.get("count")

    def get_resource_urls(self):
        resource_url = self.home_url + self.__relative_url
        return resource_url


# c = Characters()
# print(c.get_resource_urls())
# print(c.range)
# c.range = [2,10]
# print(c.range)