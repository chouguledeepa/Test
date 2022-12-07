# 1. TODO import all resource classes here
from pprint import pprint
from resources.character import Characters
from resources.films import Films
from resources.planate import Planets
from resources.species import Species
from resources.starship import Starships
from resources.vehicles import Vehicles
from utils.randgen import ThreeRandom
from utils.fetch_data import fetch_data

characters = Characters()
films = Films()
planets = Planets()
species = Species()
starships = Starships()
vehicles = Vehicles()

resources_objects = [characters, films, planets, species, starships, vehicles]
resources_names = ["characters", "films", "planets", "species", "starships", "vehicles"]

# 2. TODO get count of each resource
def get_resources_count():
    print("Count of all resources")
    resc_count = {res_name: 0 for res_name in resources_names}
    for resource, name in zip(resources_objects, resources_names):
        resc_count[name] = resource.get_count()
    return resc_count

    # print(f"Characters count - {characters.get_count()}")
    # print(f"Films count - {films.get_count()}")
    # print(f"Planets count - {planets.get_count()}")
    # print(f"Species count - {species.get_count()}")
    # print(f"Starships count - {starships.get_count()}")
    # print(f"Vehicles count - {vehicles.get_count()}")

# 3. TODO get "singular" resource urls of each resource
def get_singular_resource_urls():
    print("Getting singular resource url for each resource")
    singular_urls = []
    for resource in resources_objects:
        url = resource.get_resource_urls() + "1"
        singular_urls.append(url)
    # singular_char = characters.get_resource_urls() + "1"
    # singular_film = films.get_resource_urls() + "1"
    # singular_planet = planets.get_resource_urls() + "1"
    # singular_species = species.get_resource_urls() + "1"
    # singular_starship = starships.get_resource_urls() + "1"
    # singular_vehicle = vehicles.get_resource_urls() + "1"

    return singular_urls

# 4. TODO pull data from random 3 "singular" resource URLs
def get_random_resource_data():
    print("Pulling data for 3 random singular urls for each resource")
    resource_data = {resource_name: [] for resource_name in resources_names}
    for name, resource in zip(resources_names, resources_objects):
        for i in ThreeRandom(resource.range):
            # import pdb;pdb.set_trace()
            url = resource.get_resource_urls()+str(i)
            resource_data[name].append(fetch_data(url))

    return resource_data

def do_task_three():
    """
    1. get count of each resource
    2. get "singular" resource urls of each resource
    3. pull data from random 3 "singular" resource URLs
    """
    pprint(get_resources_count())
    pprint(get_singular_resource_urls())
    pprint(get_random_resource_data())