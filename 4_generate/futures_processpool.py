from concurrent.futures import ProcessPoolExecutor
from time import time

from factorial import factorial_func


def process_number_ProcessPool(numbers):
    quanity = len(numbers)
    start = time()
    with ProcessPoolExecutor(max_workers=quanity) as executor:
        futures = [executor.submit(factorial_func, num) for num in numbers]
        result = [f.result() for f in futures]
        finish = time() - start
        return "ProcessPool", result, finish
