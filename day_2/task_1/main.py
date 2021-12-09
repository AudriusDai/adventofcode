from typing import List

from day_2.task_1.commander.commander import apply_commands
from day_2.task_1.data import DATA
from day_2.task_1.parser.parser import parse_movement


def do_work(data: List[str]) -> int:
    commands = [parse_movement(x) for x in data]
    x, y = apply_commands(commands)

    return abs(x * y)


if __name__ == "__main__":
    r = do_work(DATA)
    print(f'Answer is: {r}')
