"""
-------      -------     --------    -------    ------
sequence execution - 13.39 seconds
"""

import random
import time
import requests


# generic decorator
def timeit(func):
    def wrapper(*args, **kwargs):
        # pre-processing
        start = time.time()
        result = func(*args, **kwargs)
        # post-processing
        print(f"[ INFO ] time to execute - {time.time() - start}")
        return result

    return wrapper


def produce_chars():
    characters = []
    for i in range(15):
        characters.append(random.randrange(1, 82))
    return characters


@timeit
def fetch_data(characters):

    output = []
    for char in characters:
        magic = "https://swapi.dev/api/people/{}/"
        url = magic.format(char)
        response = requests.get(url)
        output.append(response.status_code)

    return output


if __name__ == "__main__":
    characters_ = produce_chars()
    final = fetch_data(characters_)
    print(final)