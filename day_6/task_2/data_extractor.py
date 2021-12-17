import unittest
from typing import List


class Test(unittest.TestCase):
    def test(self):
        v = get_fish_numbers('test_data.txt')
        self.assertEqual(4, len(v))


def get_fish_numbers(file_name: str) -> List[int]:
    file = open(file_name, 'r')
    return [int(x) for x in file.readline().split(',')]


def chop_fish_numbers(chunk_size: int, file_name: str) -> List[str]:
    n = [str(x) for x in get_fish_numbers(file_name)]

    names = []
    for i in range(int(len(n) / chunk_size)):
        name = f"chopped/chop_{i}.txt"
        names.append(name)
        f = open(name, "w")
        start = i * chunk_size
        end = (i + 1) * chunk_size
        f.write(",".join(n[start:end]))
        f.close()

    return names
