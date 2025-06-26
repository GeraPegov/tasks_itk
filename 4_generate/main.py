from futures_processpool import process_number_ProcessPool
from generate import generate_data
from multi_pool import process_number_Pool
from multi_process_queue import process_number_Process
from parent_process import process_number
from tabulate import tabulate

if __name__ == "__main__":
    list_of_numbers = generate_data(int(input()))
    func = [
        process_number_Pool(list_of_numbers),
        process_number_ProcessPool(list_of_numbers),
        process_number_Process(list_of_numbers),
        process_number(list_of_numbers),
    ]

    print(tabulate(func, headers=[
        "Метод",
        "Результат выполнения",
        "Время выполнения"
        ]
        ))
