import unittest
from typing import List

from day_6.task_2.data_extractor import get_fish_numbers

DAYS = 156


class Test(unittest.TestCase):
    def test(self):
        f = get_fish_numbers('data_test.txt')
        final = grow_fish(f, 18)

        self.assertEqual(len([6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8]),
                         len(final))


def grow_fish(fish_list: List[int], day: int):
    new_fish_list = []
    # check if we have to add new fish
    for index in range(len(fish_list)):
        if fish_list[index] == 0:
            new_fish_list.append(8)
            fish_list[index] = 7

    after_list = [x - 1 for x in fish_list]
    after_list.extend(new_fish_list)

    if day in [80, 60, 40, 20, 10, 8, 3]:
        print(f'->{day}')

    if day == 1:
        return after_list

    return grow_fish(after_list, day - 1)


def fish_wrapper(chunk: List[int]) -> List[int]:
    return grow_fish([chunk], 256)


def fish_wrapper_2(chunk: List[int]) -> List[int]:
    return grow_fish([chunk], 100)


def fish_wrapper_3(chunk: List[int]) -> List[int]:
    return grow_fish([chunk], 56)
