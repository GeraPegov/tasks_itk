import random


def generate_data(n: int):
    data = random.sample(population=range(10), k=n)
    return data
