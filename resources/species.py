from resources.base import ResourceBase
from utils.fetch_data import hit_url


class Species(ResourceBase):
    """
    Planet class related functionality
    """

    def __init__(self) -> None:
        super().__init__()
        self.__relative_url = "/api/species"

    @property
    def relative_url(self):
        return self.__relative_url

    @relative_url.setter
    def relative_url(self, new_url_):
        self.__relative_url = new_url_

    def get_count(self):
        complete_url = self.home_url + self.__relative_url
        response = hit_url(complete_url)
        data = response.json()
        count = data.get("count")
        return count

    def get_sample_data(self):
        complete_url = self.home_url + self.__relative_url + "/1"
        response = hit_url(complete_url)
        data = response.json()
        return data


if __name__ == "__main__":
    p = Species()
    url = p.relative_url
    print(url)
    planet_count = p.get_count()
    print(planet_count)