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

# pydantic models
from models.DataModels.characters import Character_
from models.DataModels.Films import Film
from models.DataModels.planets import Planet_
from models.DataModels.species import  Species_
from models.DataModels.starship import Starship_
from models.DataModels.vehicle import Vehicle_

# resource-classes
from resources.planate import Planets
from resources.films import Films
from resources.character import Characters
from resources.vehicles import Vehicles
from resources.species import Species
from resources.starship import Starships

from dal.sample import insert_resource


if __name__ == "__main__":

    film_data = Film().get_sample_data(id_=1)
    film_data = Films(**film_data)

    film_columns = ["title", "opening_crawl",
                    "director", "producer", "release_date", "created", "edited",
                    "url"]
    breakpoint()

    film_values = [film_data.title,
                   film_data.opening_crawl, film_data.director,
                   film_data.producer, film_data.release_date,
                   film_data.created.strftime("YYYY-MM-DD"),
                   film_data.edited.strftime("YYYY-MM-DD"),
                   film_data.url]

    result = insert_resource(
        "film", "film_id", film_data.episode_id,
        film_columns, film_values
    )

#
# from dal.sample import insert_resource
#
#
# if __name__ == "__main__":
#
#     film_data = Film().get_sample_data(id_=1)
#     film_data = Film_(**film_data)
#
#     film_columns = ["title", "opening_crawl",
#                     "director", "producer", "release_date", "created", "edited",
#                     "url"]
#
#     film_values = [film_data.title,
#                    film_data.opening_crawl, film_data.director,
#                    film_data.producer, film_data.release_date,
#                    film_data.created.strftime("YYYY-MM-DD"),
#                    film_data.edited.strftime("YYYY-MM-DD"),
#                    film_data.url]
#
#     result = insert_resource("film", "film_id", film_data.episode_id, film_columns, film_values)
