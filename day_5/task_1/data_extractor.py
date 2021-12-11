import unittest
from typing import List

from day_5.task_1.vector import Vector


class Test(unittest.TestCase):
    def test(self):
        v = get_vectors('test_data.txt')
        self.assertEqual(10, len(v))

        t = [x for x in v if not x.is_diagonal()]
        self.assertEqual(8, len(t))


def get_vectors(file_name: str) -> List[Vector]:
    file1 = open(file_name, 'r')
    raw_vectors = file1.readlines()

    vectors: List[Vector] = []
    for raw_vector in raw_vectors:
        points = raw_vector.split(' -> ')
        point_1 = points[0].split(',')
        point_2 = points[1].split(',')
        vectors.append(Vector(
            x_1=int(point_1[0]),
            y_1=int(point_1[1]),
            x_2=int(point_2[0]),
            y_2=int(point_2[1]),
        ))

    return vectors
