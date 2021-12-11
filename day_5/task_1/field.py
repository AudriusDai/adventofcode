import unittest
from typing import Dict, Tuple

from day_5.task_1.data_extractor import get_vectors
from day_5.task_1.vector import Vector


class Test(unittest.TestCase):
    def test(self):
        f = Field()
        vectors = [x for x in get_vectors('test_data.txt') if not x.is_diagonal()]
        for v in vectors:
            f.apply_vector(v)
        return


class Field:
    field: Dict[Tuple[int, int], int]

    def __init__(self):
        self.field = {}

    def get_dangerous_points_count(self) -> int:
        r = 0
        for value in self.field.values():
            if value >= 2:
                r += 1

        return r

    def apply_vector(self, v: Vector) -> None:
        if v.is_horizontal():
            return self._apply_horizontal(v)
        elif v.is_vertical():
            return self._apply_vertical(v)
        else:
            raise Exception('implementation not found')

    def _apply_horizontal(self, v: Vector) -> None:
        y = v.y_1
        start = 0
        end = 0
        if v.x_1 <= v.x_2:
            start = v.x_1
            end = v.x_2
        else:
            start = v.x_2
            end = v.x_1

        while start <= end:
            if not self.field.get((start, y)):
                self.field[(start, y)] = 1
            else:
                self.field[(start, y)] += 1

            start += 1
        return

    def _apply_vertical(self, v: Vector) -> None:
        x = v.x_1
        start = 0
        end = 0
        if v.y_1 <= v.y_2:
            start = v.y_1
            end = v.y_2
        else:
            start = v.y_2
            end = v.y_1

        while start <= end:
            if not self.field.get((x, start)):
                self.field[(x, start)] = 1
            else:
                self.field[(x, start)] += 1

            start += 1
        return
