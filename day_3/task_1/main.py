from typing import List
from day_3.task_1.data import DATA


def get_most_repeated_bits(data: List[str]) -> str:
    final = ''
    for i in range(len(data[0])):
        zeroes = 0
        ones = 0
        for j in range(len(data)):
            if int(data[j][i]) == 0:
                zeroes += 1
            else:
                ones += 1

        if ones >= zeroes:
            final += '1'
        else:
            final += '0'
    return final


def get_least_repeated_bits(data: List[str]) -> str:
    final = ''
    for i in range(len(data[0])):
        zeroes = 0
        ones = 0
        for j in range(len(data)):
            if int(data[j][i]) == 0:
                zeroes += 1
            else:
                ones += 1

        if ones >= zeroes:
            final += '0'
        else:
            final += '1'
    return final


def do_work(data: List[str]) -> int:
    gamma = int(get_most_repeated_bits(data), 2)
    epsilon = int(get_least_repeated_bits(data), 2)
    power_consumption = gamma * epsilon

    return power_consumption


if __name__ == "__main__":
    r = do_work(DATA)
    print(f'Answer is: {r}')
