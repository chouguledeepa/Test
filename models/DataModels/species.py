"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List,Union, Optional
from decimal import Decimal
from models.Basemodel import Base
from pprint import pprint
from pydantic import validator



class Species_(Base):
    """ Pydantic model class meant to validate the data for `Species` object from
        single resource endpoint from starwars API.
    """

    # # attribute fields
    # average_height: str
    # average_lifespan: str
    # classification: str
    # designation: str
    # eye_colors: str
    # hair_colors: str
    # homeworld: Optional[str]
    # language: str
    # name: str
    # skin_colors: str
    #
    # # relationship attribute fields
    # people: Optional[List[str]]
    # films: Optional[List[str]]


    class Species(Base):
        name: str
        classification: str
        designation: str
        average_height: Union[int, str]
        skin_colors: str
        hair_colors: str
        eye_colors: str
        average_lifespan: Union[int, str]
        homeworld: Optional[str]
        people: List[str]
        films: List[str]

        @validator("homeworld")
        def validate_homeworld(cls, homeworld):
            if isinstance(homeworld, type(None)):
                cls.homeworld = 'Null'
                return cls.homeworld

    if __name__ == "__main__":
        speci_data = {
            "name": "Human",
            "classification": "mammal",
            "designation": "sentient",
            "average_height": "180",
            "skin_colors": "caucasian, black, asian, hispanic",
            "hair_colors": "blonde, brown, black, red",
            "eye_colors": "brown, blue, green, hazel, grey, amber",
            "average_lifespan": "120",
            "homeworld": "https://swapi.dev/api/planets/9/",
            "language": "Galactic Basic",
            "people": [
                "https://swapi.dev/api/people/66/",
                "https://swapi.dev/api/people/67/",
                "https://swapi.dev/api/people/68/",
                "https://swapi.dev/api/people/74/"
            ],
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/4/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "created": "2014-12-10T13:52:11.567000Z",
            "edited": "2014-12-20T21:36:42.136000Z",
            "url": "https://swapi.dev/api/species/1/"
        }

        speci_obj = Species(**speci_data)
        pprint(dict(speci_obj))