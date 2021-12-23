import time
from pprint import pprint
from typing import List, Tuple


def fold_x(coordinates: List[Tuple[int, int]], x_line: int) -> List[Tuple[int, int]]:
    temp_coordinates: List[Tuple[int, int]] = []
    for c in coordinates:
        x, y = c
        if x < x_line:
            temp_coordinates.append(c)
            continue

        new_x = x_line - (x - x_line)
        temp_coordinates.append((new_x, y))

    return list(set(temp_coordinates))


def fold_y(coordinates: List[Tuple[int, int]], y_line: int) -> List[Tuple[int, int]]:
    temp_coordinates: List[Tuple[int, int]] = []
    for c in coordinates:
        x, y = c
        if y < y_line:
            temp_coordinates.append(c)
            continue

        new_y = y_line - (y - y_line)
        temp_coordinates.append((x, new_y))

    return list(set(temp_coordinates))


def main() -> int:
    coordinates: List[Tuple[int, int]] = [tuple([int(x) for x in line.strip().split(',')]) for line in
                                          open('data.txt', 'r').readlines()]

    coordinates = fold_x(coordinates, 655)

    pprint(coordinates)

    return len(coordinates)


if __name__ == "__main__":
    tic = time.perf_counter()
    r = main()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
