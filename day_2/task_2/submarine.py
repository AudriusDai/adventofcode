from typing import Tuple

from day_2.task_2.parser.parser import Command


class Submarine:
    aim: int
    horizontal: int
    depth: int

    def __init__(self):
        self.aim = 0
        self.horizontal = 0
        self.depth = 0

    def apply_command(self, command: Tuple[str, int]):
        action, steps = command

        if action == Command.Forward.value:
            self.horizontal += steps
            self.depth += steps * self.aim
        elif action == Command.Down.value:
            self.aim += steps
        elif action == Command.Up.value:
            self.aim -= steps

    def get_final(self):
        return self.horizontal * self.depth
    