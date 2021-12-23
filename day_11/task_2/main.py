import time
from pprint import pprint
from typing import List


def flash_first_octopus_found(f: List[List[int]]) -> None:
    found = False
    for x in range(len(f)):
        if found:
            break
        for y in range(len(f[0])):
            if found:
                break
            if f[x][y] > 9:
                found = True
                f[x][y] = 0
                # horizontal & vertical
                if x - 1 >= 0:
                    f[x - 1][y] = f[x - 1][y] + 1 if f[x - 1][y] not in [0, 10] else f[x - 1][y]
                if x + 1 < len(f):
                    f[x + 1][y] = f[x + 1][y] + 1 if f[x + 1][y] not in [0, 10] else f[x + 1][y]
                if y - 1 >= 0:
                    f[x][y - 1] = f[x][y - 1] + 1 if f[x][y - 1] not in [0, 10] else f[x][y - 1]
                if y + 1 < len(f[0]):
                    f[x][y + 1] = f[x][y + 1] + 1 if f[x][y + 1] not in [0, 10] else f[x][y + 1]

                # diagonal
                if x - 1 >= 0 and y - 1 >= 0:
                    f[x - 1][y - 1] = f[x - 1][y - 1] + 1 if f[x - 1][y - 1] not in [0, 10] else f[x - 1][y - 1]
                if x - 1 >= 0 and y + 1 < len(f[0]):
                    f[x - 1][y + 1] = f[x - 1][y + 1] + 1 if f[x - 1][y + 1] not in [0, 10] else f[x - 1][y + 1]
                if x + 1 < len(f) and y - 1 >= 0:
                    f[x + 1][y - 1] = f[x + 1][y - 1] + 1 if f[x + 1][y - 1] not in [0, 10] else f[x + 1][y - 1]
                if x + 1 < len(f) and y + 1 < len(f[0]):
                    f[x + 1][y + 1] = f[x + 1][y + 1] + 1 if f[x + 1][y + 1] not in [0, 10] else f[x + 1][y + 1]


def are_all_ready_to_flash(f: List[List[int]]) -> bool:
    for line in f:
        for c in line:
            if c > 0:
                return False

    return True


def add_one_to_all(octopus_field: List[List[int]]) -> None:
    for x in range(len(octopus_field)):
        for y in range(len(octopus_field[0])):
            if octopus_field[x][y] > 9:
                continue
            else:
                octopus_field[x][y] += 1


def any_octopus_ready_to_flash(octopus_field: List[List[int]]) -> bool:
    for line in octopus_field:
        for c in line:
            if c > 9:
                return True

    return False


def main() -> int:
    octopus_field: List[List[int]] = [[int(s) for s in line.strip()] for line in open('data.txt', 'r').readlines()]
    step = 0
    print('initial field of octopuses:')
    pprint(octopus_field)
    total_flashes = 0
    while not are_all_ready_to_flash(octopus_field):
        step += 1
        print(f'step {step}:')
        add_one_to_all(octopus_field)
        while any_octopus_ready_to_flash(octopus_field):
            flash_first_octopus_found(octopus_field)
            total_flashes += 1

        pprint(octopus_field)

    return step


if __name__ == "__main__":
    tic = time.perf_counter()
    r = main()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
