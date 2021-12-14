import unittest

import gmpy


class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(Vector(x_1=1, y_1=1, x_2=2, y_2=2).is_diagonal())
        self.assertTrue(Vector(x_1=0, y_1=0, x_2=2, y_2=2).is_diagonal())
        self.assertFalse(Vector(x_1=0, y_1=0, x_2=2, y_2=3).is_diagonal())


class Vector:
    x_1: int
    y_1: int
    x_2: int
    y_2: int

    def __init__(self, x_1: int, y_1: int, x_2: int, y_2: int):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2

    def is_vertical(self) -> bool:
        return self.x_1 == self.x_2

    def is_horizontal(self) -> bool:
        return self.y_1 == self.y_2

    def is_diagonal(self) -> bool:
        x = abs(self.x_1 - self.x_2)
        y = abs(self.y_1 - self.y_2)
        return x == y
