from typing import Tuple, List

from day_2.task_1.parser.parser import Command


def apply_commands(commands: List[Tuple[str, int]]) -> (int, int):
    x = 0
    y = 0

    for command, steps in commands:
        if command == Command.Forward.value:
            x += steps
        elif command == Command.Up.value:
            y += steps
        elif command == Command.Down.value:
            y -= steps

    return x, y
