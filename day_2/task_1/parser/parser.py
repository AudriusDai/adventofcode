from enum import Enum


class Command(Enum):
    Forward = 'forward'
    Up = 'up'
    Down = 'down'


def parse_movement(command: str) -> (str, int):
    items = command.split(' ')
    if len(items) < 2:
        raise Exception('impossible to parse movement ' + command)

    if items[0] not in [e.value for e in Command]:
        raise Exception('unrecognized command ' + items[0])

    return items[0], int(items[1])
