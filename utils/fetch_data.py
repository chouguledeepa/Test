import requests
import logging
from typing import List, Optional
from requests.models import Response

from requests import HTTPError


# logging configuration
logging.basicConfig(filename="utils/example.log", encoding="utf-8", level=logging.INFO)


def mylogger(func):
    def wrapper(url, **kwargs):
        try:
            logging.info(f"we are hitting URL - {url}")
            result_ = func(url)
            logging.info(f"success - {result_.status_code}")
        except Exception:
            logging.error(f"there are issues fetching details")

        return result_

    return wrapper


@mylogger
def hit_url(url: str) -> Optional[Response]:

    response = requests.get(url)
    if response.status_code != 200:
        response.raise_for_status()
    else:
        return response


# TODO - try with following function as well.

# @mylogger
# def hit_url(url):
#
#     try:
#         response = requests.get(url)
#         return response
#     except HTTPError as e:
#         logging.error(f"Response not generated from {url}. "
#                       f"Please test in postman first")
#         return {}
#


def fetch_data(urls: List) -> List:
    """fetching data from urls"""

    data = []
    for url in urls:
        res = hit_url(url)
        data.append(res.json())

    return data


if __name__ == "__main__":
    result = ["https://swapi.dev/api/people/1/"]
    output = fetch_data(result)
    print(output)