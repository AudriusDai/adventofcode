import time
from pprint import pprint
from typing import List


class Cave:
    def __init__(self, name: str):
        self.name = name
        self.neighbour_caves = []

    def add_neighbour_cave(self, cave) -> None:
        if self.get_name() == cave.get_name():
            return

        exist = [c for c in self.neighbour_caves if c.get_name() == cave.get_name()]
        if not exist:
            self.neighbour_caves.append(cave)

    def is_big_cave(self):
        return self.name.isupper()

    def get_name(self):
        return self.name

    def __repr__(self):
        return self.name


def has_over_two_same_small_caves(caves: List[Cave]) -> bool:
    temp = [c for c in caves if c.get_name() not in ['start', 'end'] and not c.is_big_cave()]
    for i in range(len(temp)):
        counter = 0
        for c in temp:
            if c.get_name() == temp[i].get_name():
                counter += 1
        if counter > 2:
            return True

    return False


def has_more_than_two_double_caves(caves: List[Cave]) -> bool:
    temp = [c for c in caves if c.get_name() not in ['start', 'end'] and not c.is_big_cave()]
    total = 0
    for i in range(len(temp)):
        counter = 0
        for c in temp:
            if c.get_name() == temp[i].get_name():
                counter += 1
        if counter >= 2:
            total += 1

    total = total / 2
    return int(total) > 1


def find_path(paths: List[List[Cave]], prefix_path: List[Cave], neighbours: List[Cave]):
    for neighbour in [n for n in neighbours if n.get_name() != 'start']:
        prefix_path_copy = prefix_path.copy()

        exist = [n for n in prefix_path_copy if n.get_name() == neighbour.get_name()]
        if exist:
            if not neighbour.is_big_cave():
                if len(exist) >= 2:
                    continue
                l = prefix_path_copy[:]
                l.append(neighbour)
                if has_more_than_two_double_caves(l):
                    continue

        prefix_path_copy.append(neighbour)
        if neighbour.get_name() == 'end':
            paths.append(prefix_path_copy)
        else:
            find_path(paths, prefix_path_copy, neighbour.neighbour_caves)


def main() -> int:
    raw_cave_connections: List[List[str]] = [line.strip().split('-') for line in open('data.txt', 'r').readlines()]
    caves: List[Cave] = []
    cave_connections: List[List[Cave]] = []

    for raw_connection in raw_cave_connections:
        connection = []
        for raw_cave_name in raw_connection:
            existing_cave = [c for c in caves if c.get_name() == raw_cave_name]
            if existing_cave:
                connection.append(existing_cave[0])
            else:
                cave = Cave(raw_cave_name)
                connection.append(cave)
                caves.append(cave)
        cave_connections.append(connection)

    for conn in cave_connections:
        conn[0].add_neighbour_cave(conn[1])
        conn[1].add_neighbour_cave(conn[0])

    # pprint(cave_connections)
    # for cave in caves:
    #     pprint(f'Cave {cave}, neighbours: {cave.neighbour_caves}')

    start_cave: Cave = [c for c in caves if c.get_name() == 'start'][0]
    print(f'start cave - {start_cave}')

    paths: List[List[Cave]] = []

    find_path(paths, [start_cave], start_cave.neighbour_caves)

    pprint(paths)

    return len(paths)


if __name__ == "__main__":
    tic = time.perf_counter()
    r = main()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
