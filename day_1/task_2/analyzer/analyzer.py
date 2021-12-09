from typing import List


def get_count_of_greater_than_previous(items: List[int]):
    counter = 0
    if not items:
        return counter

    for i in range(len(items)):
        if i == 0:
            continue
        if items[i] > items[i - 1]:
            counter += 1

    return counter
