import unittest

from day_2.task_1.parser.parser import parse_movement, Command


class Test(unittest.TestCase):
    def test_parse_command(self):
        self.assertEqual((Command.Forward.value, 100), parse_movement('forward 100'))

    def test_parse_command_unrecognized(self):
        with self.assertRaises(Exception) as context:
            parse_movement('x 99')

        self.assertTrue('unrecognized' in str(context.exception))
