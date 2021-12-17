import unittest
from typing import List

from day_6.task_1.data_extractor import get_fish_numbers


class Test(unittest.TestCase):
    def test(self):
        f = get_fish_numbers('data_test.txt')
        final = grow_fish(f, 18)

        self.assertEqual(len([6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8]),
                         len(final))


def grow_fish(fish_list: List[int], day: int) -> List[int]:
    new_fish_list = []
    # check if we have to add new fish
    for index in range(len(fish_list)):
        if fish_list[index] == 0:
            new_fish_list.append(8)
            fish_list[index] = 7

    after_list = [x - 1 for x in fish_list]
    after_list.extend(new_fish_list)
    # print(f'day {day}: {after_list}')
    if day == 1:
        return after_list

    return grow_fish(after_list, day - 1)
