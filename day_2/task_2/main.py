from typing import List

from day_2.task_2.data import DATA
from day_2.task_2.parser.parser import parse_movement
from day_2.task_2.submarine import Submarine


def do_work(data: List[str]) -> int:
    commands = [parse_movement(x) for x in data]
    submarine = Submarine()
    for command in commands:
        submarine.apply_command(command)

    return submarine.get_final()


if __name__ == "__main__":
    r = do_work(DATA)
    print(f'Answer is: {r}')
