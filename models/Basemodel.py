"""
this model shows another pyndatic model resources aka datamodels

"""
from  pydantic import BaseModel
from  datetime import datetime

class Base(BaseModel):

    """
    comman attributes for all model resources
    """
    created:datetime
    edited:datetime
    url:str

if __name__ == '__main__':
    data = {
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-20T21:17:56.891000Z",
        "url": "https://swapi.dev/api/people/1/"
    }
    obj = Base(**data)
    print(obj.created)
    print(type(obj.created))
    print("*******" *10)
    print(obj)