import unittest

from day_1.task_2.grouper.grouper import group_data


class Test(unittest.TestCase):
    def test_group_data(self):
        self.assertEqual([3], group_data([1, 2], 2))
        self.assertEqual([3, 5], group_data([1, 2, 3], 2))
        self.assertEqual([3, 5, 7], group_data([1, 2, 3, 4], 2))
        self.assertEqual([6, 9], group_data([1, 2, 3, 4], 3))

    def test_group_data_error(self):
        with self.assertRaises(Exception) as context:
            group_data([1, 2], 3)

        self.assertTrue('group size cannot be greater than data provided' in str(context.exception))
