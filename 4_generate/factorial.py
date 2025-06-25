import math


def factorial_func(n):
    return math.factorial(n)


def factorial_queue(n, q):
    data = math.factorial(n)
    q.put(data)
