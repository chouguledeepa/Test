"""
{
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
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/3/",
        "https://swapi.dev/api/films/6/"
    ],
    "species": [],
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
}``

"""
# from  pydantic import BaseModel
# from models.Basemodel import Base
#
# from typing import Optional, List
#
# class Character(Base):
#     name:str
#     height: str
#     mass: str
#     hair_color: str
#     skin_color: str
#     eye_color: str
#     birth_year:str
#     gender:str
#     homeworld:str
#
#     film:Optional[List[str]]
#     species:Optional[list[str]]
#     vehicles:Optional[list[str]]
#     speciships:Optional[list[str]]

"""

from pydantic import BaseModel
from pydantic import BaseModel, validator
from models.basemodel import Base

from typing import List, Optional
@@ -23,3 +23,13 @@ class Character_(Base):
    starships: Optional[List[str]]
    films: Optional[List[str]]
    vehicles: Optional[List[str]]

    @validator("height")
    def height_validation(cls):
        if isinstance(cls.height, str):
            height = int(cls.height)
            height = height / 100
            cls.height = height
            return cls.height
        else:
            raise ValueError('height cannot be converted')"""

from pydantic import BaseModel
from pydantic import BaseModel, validator
from models.Basemodel import Base

from typing import List, Optional
class Character_(Base):
    starships: Optional[List[str]]
    films: Optional[List[str]]
    vehicles: Optional[List[str]]

    @validator("height")
    def height_validation(cls):
        if isinstance(cls.height, str):
            height = int(cls.height)
            height = height / 100
            cls.height = height
            return cls.height
        else:
            raise ValueError('height cannot be converted')