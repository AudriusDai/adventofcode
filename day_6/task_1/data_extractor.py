import unittest
from typing import List


class Test(unittest.TestCase):
    def test(self):
        v = get_fish_numbers('test_data.txt')
        self.assertEqual(4, len(v))


def get_fish_numbers(file_name: str) -> List[int]:
    file = open(file_name, 'r')
    return [int(x) for x in file.readline().split(',')]
