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
    coordinates = fold_y(coordinates, 447)
    coordinates = fold_x(coordinates, 327)
    coordinates = fold_y(coordinates, 223)
    coordinates = fold_x(coordinates, 163)
    coordinates = fold_y(coordinates, 111)
    coordinates = fold_x(coordinates, 81)
    coordinates = fold_y(coordinates, 55)
    coordinates = fold_x(coordinates, 40)
    coordinates = fold_y(coordinates, 27)
    coordinates = fold_y(coordinates, 13)
    coordinates = fold_y(coordinates, 6)

    for y in range(6):
        s = ''
        for i in range(40):
            s += '#' if (i, y) in coordinates else '_'
        print(s)

    pprint(coordinates)

    return len(coordinates)


if __name__ == "__main__":
    tic = time.perf_counter()
    r = main()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
