# """
# TODO
# 1. pull data for the movie "A New Hope"
# 2. Replace the data for each of the endpoint listed in the JSON object
#  and insert that data into respective database tables
#  (using following instructions)
#     (For example - "A New Hope" has following resource endpoints)
#         - characters
#         - planets
#         - vehicles
#         - starships
#         - species
# 3. Convert height and weight in each character to standard units
# 4. You have to remove all cross-referencing URLs from each resource
# """
#
# # pydantic models
# from models.DataModels.characters import Character_
# from models.DataModels.Films import Film
# from models.DataModels.planets import Planet_
# from models.DataModels.species import  Species_
# from models.DataModels.starship import Starship_
# from models.DataModels.vehicle import Vehicle_
#
# # resource-classes
# from resources.planate import Planets
# from resources.films import Films
# from resources.character import Characters
# from resources.vehicles import Vehicles
# from resources.species import Species
# from resources.starship import Starships
#
# from dal.sample import insert_resource
#
#
# if __name__ == "__main__":
#
#     film_data = Film().get_sample_data(id_=1)
#     film_data = Films(**film_data)
#
#     film_columns = ["title", "opening_crawl",
#                     "director", "producer", "release_date", "created", "edited",
#                     "url"]
#     breakpoint()
#
#     film_values = [film_data.title,
#                    film_data.opening_crawl, film_data.director,
#                    film_data.producer, film_data.release_date,
#                    film_data.created.strftime("YYYY-MM-DD"),
#                    film_data.edited.strftime("YYYY-MM-DD"),
#                    film_data.url]
#
#     result = insert_resource(
#         "film", "film_id", film_data.episode_id,
#         film_columns, film_values
#     )

#
# from dal.sample import insert_resource

"""
TODO
1. pull data for the movie "A New Hope"
2. Replace the data for each of the endpoint listed in the JSON object
 and insert that data into respective database tables
 (using following instructions)
    (For example - "A New Hope" has following resource endpoints)
        - characters
        - planets
        - vehicles
        - starships
        - species
3. Convert height and weight in each character to standard units
4. You have to remove all cross-referencing URLs from each resource
"""

from datetime import datetime
from multiprocessing.pool import ThreadPool
import pydantic
from typing import List, Dict
from resources.films import Film
from utils.fetch_data import fetch_data
from models.DataModels.Films import Film as Films_
from models.DataModels.characters import Characters
from models.DataModels.planets import Planet_
from models.DataModels.vehicle import Vehicle_
from models.DataModels.species import Species_
from models.DataModels.starship import Starship_
from dal.dml import insert_resource
from dal.db_con_helper import insert_resource


def remove_cross_reference(data_set: "pydantic datamodel object") -> Dict:
    """
    1. Takes pydantic datamodel object as argument of any resource.
    2. Converts it to dictionary data type.
    3. Removes cross-reference fields if any. (ex., character["url1","url2"])
    4. Converts datetime object to string date in format - "YYYY-MM-DD"
    5. If any field contain None value, converts it into Null, so that it can be inserted into the database.
    6. Returns this formatted dictionary.
    :param data_set: validated pydantic data model object
    :return: Dictionary
    """
    data_set = dict(data_set)
    new_data = data_set.copy()
    for key, value in data_set.items():
        if isinstance(value, list):     # removing cross-reference fields from data object
            new_data.pop(key)
        elif isinstance(value, datetime):   # converting datetime object to str date
            new_data[key] = new_data[key].strftime("%Y-%m-%d")
        elif isinstance(value, type(None)):  # replace None with Null
            new_data[key] = 'Null'

    return new_data


def fetch_url_data(url_list: List[str]) -> List[Dict]:
    """
    1. Hits each url in url list.
    2. Uses ThreadPool to hit urls concurrently and fetches data for each url using map function.
    3. Returns list of dictionary (endpoints data) of each url/api endpoint
    :param url_list: list containing api endpoints
    :return: list of respective endpoint data in json/dict format
    """
    # fetching data for each resource endpoint from film_1
    pool = ThreadPool(25)
    url_data = pool.map(fetch_data, url_list)  # Return data for all urls.
    # map() function returns list
    return url_data


def validate_data(resource: Dict, validator: "pydantic datamodel") -> List[Dict]:
    """
    For each data in 'resource'-
    1. Does data validation using pydantic datamodel - 'validator'
    2. Removes all fields containing cross-reference urls
    3. appends to new list
    Returns list of dictionary(validated data)
    :param resource: Dictionary of resource data fetched from swapi in json format
    :param validator: pydantic datamodel for data validation
    :return: List of validated data in the Dictionary format
    """
    new_data = []
    for data in resource:
        # breakpoint()
        data = validator(**data)    # validates each url data using pydantic datamodels
        new = remove_cross_reference(data)  # removes cross-reference fields from each url data
        new_data.append(new)
    return new_data


if __name__ == "__main__":
    # pull data for the movie "A New Hope"
    # breakpoint()
    film_data = Film().get_sample_data()
    film_data = Films_(**film_data)

    # fetching urls of each resource in film_1
    charlist = film_data.characters
    planetlist = film_data.planets
    specieslist = film_data.species
    starshipslist = film_data.starships
    vehiclelist = film_data.vehicles

    # Replace the data for each of the endpoint listed in the JSON object.
    char_data = fetch_url_data(charlist)
    planet_data = fetch_url_data(planetlist)
    species_data = fetch_url_data(specieslist)
    starships_data = fetch_url_data(starshipslist)
    vehicle_data = fetch_url_data(vehiclelist)

    # remove all cross-referencing URLs from each resource and validate data using datamodels
    char_data = validate_data(char_data, Characters)
    planet_data = validate_data(planet_data, Planet_)
    species_data = validate_data(species_data, Species_)
    starships_data = validate_data(starships_data, Starship_)
    vehicle_data = validate_data(vehicle_data, Vehicle_)

    #  and insert that data into respective database tables
    char_table = "characters"
    for data in char_data:
        print(f"rows affected - {insert_resource(char_table, data)}")

    planet_table = "planet"
    for data in planet_data:
        print(f"rows affected - {insert_resource(planet_table, data)}")

    vehicle_table = "vehicle"
    for data in vehicle_data:
        print(f"rows affected - {insert_resource(vehicle_table, data)}")

    starship_table = "starship"
    for data in starships_data:
        print(f"rows affected - {insert_resource(starship_table, data)}")

    species_table = "species"
    # breakpoint()
    for data in species_data:
        print(f"rows affected - {insert_resource(species_table, data)}")

    film_table = "film"
    film_data = remove_cross_reference(film_data)
    # breakpoint()
    print(f"rows affected - {insert_resource(film_table, film_data)}")
