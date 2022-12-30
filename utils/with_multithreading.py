"""
-------      -------     --------    -------    ------
sequence execution =>  13.39 seconds
concurrent execution with 15 threads => 1.31 seconds
concurrent execution with 5 threads => 2.84 seconds
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


def get_urls(characters):
    """to produce list of urls based on characters"""

    urls = []
    for char in characters:
        magic = "https://swapi.dev/api/people/{}/"
        url = magic.format(char)
        urls.append(url)
    return urls


def hit_url(url):
    """simply send HTTP request per URL"""

    response = requests.get(url)
    return response.status_code


@timeit
def main(characters):

    # create thread-pool
    from multiprocessing.pool import ThreadPool

    pool_size = 15
    pool = ThreadPool(pool_size)

    urls = get_urls(characters)
    result = pool.map(hit_url, urls)
    return result


if __name__ == "__main__":
    characters_ = produce_chars()
    final = main(characters_)
    print(final)