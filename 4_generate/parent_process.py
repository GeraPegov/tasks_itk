import math
from time import time


def process_number(numbers):
    start = time()
    result = [math.factorial(num) for num in numbers]
    finish = time() - start
    return "Родительский процесс", result, finish
