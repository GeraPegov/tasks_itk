from multiprocessing import Pool, cpu_count
from time import time

from factorial import factorial_func


def process_number_Pool(numbers):
    start = time()
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(factorial_func, numbers)
        finish = time() - start
        return "Pool", results, finish
