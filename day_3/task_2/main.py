from typing import List
from day_3.task_2.data import DATA


def get_oxygen_generator_rating(data: List[str], start_at: int = 0) -> int:
    next_at = start_at + 1
    if len(data) == 1:
        return int(data[0], 2)

    zeroes = []
    ones = []
    for j in range(len(data)):
        if int(data[j][start_at]) == 0:
            zeroes.append(data[j])
        else:
            ones.append(data[j])

    if len(ones) >= len(zeroes):
        return get_oxygen_generator_rating(ones, next_at)
    else:
        return get_oxygen_generator_rating(zeroes, next_at)


def get_co2_scrubber_rating(data: List[str], start_at: int = 0) -> int:
    next_at = start_at + 1
    if len(data) == 1:
        return int(data[0], 2)

    zeroes = []
    ones = []
    for j in range(len(data)):
        if int(data[j][start_at]) == 0:
            zeroes.append(data[j])
        else:
            ones.append(data[j])

    if len(ones) >= len(zeroes):
        return get_co2_scrubber_rating(zeroes, next_at)
    else:
        return get_co2_scrubber_rating(ones, next_at)


def do_work(data: List[str]) -> int:
    oxygen_generator_rating = get_oxygen_generator_rating(data)
    co2_scrubber_rating = get_co2_scrubber_rating(data)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating

    return life_support_rating


if __name__ == "__main__":
    r = do_work(DATA)
    print(f'Answer is: {r}')
