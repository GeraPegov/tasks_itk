def search(number: int):
    example_list = [1, 2, 3, 45, 356, 569, 600, 705, 923]
    left, right = 0, len(example_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if example_list[mid] == number:
            return True
        if example_list[mid] < number:
            right = mid - 1
        else:
            left = mid + 1
    return False
