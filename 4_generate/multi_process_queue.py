from multiprocessing import Process, Queue
from time import time

from factorial import factorial_queue


def process_number_Process(numbers):
    start = time()
    q = Queue()
    tasks = []
    for num in numbers:
        p = Process(target=factorial_queue, args=(num, q))
        p.start()
        tasks.append(p)
    results = [q.get() for _ in numbers]
    for p in tasks:
        p.join()
    finish = time() - start
    return "Process, Queue", results, finish

