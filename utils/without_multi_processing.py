"""
42 elements - 19 seconds with single process (linear)
"""

import time


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


def compute_intensive_work(range_):
    result = [i**3 for i in range(range_)]
    return result


@timeit
def main():
    large_number_range = [2000000, 2000000, 2000000, 2000000, 2000000, 2000000]

    for range_ in large_number_range:
        compute_intensive_work(range_)


if __name__ == "__main__":
    main()