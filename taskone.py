from utils.randgen import RandomCharacters
from utils.fetch_data import fetch_data

home_url = "https://swapi.dev"  # swapi website
relative_url = "/api/people/{0}"  # magic string


def do_task_one():
    """
    get details from 15 random characters from [1 to 82]
    :return:
    """
    for character in RandomCharacters():  # generating random character from
        # RandomCharacter generator

        absolute_url = home_url + relative_url.format(
            character)  # creating url from  # each character in RandomCharacters() generator
    print(fetch_data(absolute_url))  # etting all details from character url
    print("#######" * 25)
