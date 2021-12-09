import unittest

from day_1.task_2.analyzer.analyzer import get_count_of_greater_than_previous


class Test(unittest.TestCase):
    def test_group_data(self):
        self.assertEqual(0, get_count_of_greater_than_previous([]))
        self.assertEqual(0, get_count_of_greater_than_previous([1]))
        self.assertEqual(0, get_count_of_greater_than_previous([2, 1]))
        self.assertEqual(1, get_count_of_greater_than_previous([1, 2]))
        self.assertEqual(2, get_count_of_greater_than_previous([1, 2, 3]))
        self.assertEqual(3, get_count_of_greater_than_previous([1, 2, 3, 2, 3]))
