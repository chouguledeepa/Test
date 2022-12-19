"""
42 elements - 11.75 seconds with 3 processes (multi-processing)
42 elements - 7.3 seconds with 8 processes (multi-processing)
42 elements - 8 seconds with 20 processes (multi-processing)
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
    large_number_range = [2000000, 2000000, 2000000, 2000000, 2000000, 2000000,]


    import multiprocessing
    pool_ = multiprocessing.Pool(20)
    pool_.map(compute_intensive_work, large_number_range)


if __name__ == "__main__":
    main()