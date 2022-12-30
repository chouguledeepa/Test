from datetime import datetime
from dal.sample import get_db_conn, insert_resource
from models.datamodels.characters import Characters
from task_four import remove_cross_reference


# sp_data = {'species_id': 101, 'average_height': "2 cm", 'average_lifespan': "70 days", 'classification': "common"}

ch_data = {
    "name": "Luke Skywalker",
    "height": "172",
    "mass": "77",
    "hair_color": "blond",
    "skin_color": "fair",
    "eye_color": "blue",
    "birth_year": "19BBY",
    "gender": "male",
    "homeworld": "https://swapi.dev/api/planets/1/",
    "films": [
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/6/",
        "https://swapi.dev/api/films/3/",
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/7/"
    ],
    "species": [
        "https://swapi.dev/api/species/1/"
    ],
    "vehicles": [
        "https://swapi.dev/api/vehicles/14/",
        "https://swapi.dev/api/vehicles/30/"
    ],
    "starships": [
        "https://swapi.dev/api/starships/12/",
        "https://swapi.dev/api/starships/22/"
    ],
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-20T21:17:56.891000Z",
    "url": "https://swapi.dev/api/people/1/"
}
ch_data = Characters(**ch_data)
# print(insert_resource("species_sample", sp_data))
ch_data = remove_cross_reference(ch_data)
print(insert_resource("characters", dict(ch_data)))