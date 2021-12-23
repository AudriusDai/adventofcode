import time
from pprint import pprint
from typing import List, Tuple


def main() -> int:
    polymer = 'KKOSPHCNOCHHHSPOBKVF'
    values: List[List[str]] = [line.strip().split(' -> ') for line in open('data.txt', 'r').readlines()]
    formulas = {v[0]: v[1] for v in values}

    map = {}
    for i in range(len(polymer) - 1):
        if map.get(polymer[i: i + 2]):
            map[polymer[i: i + 2]] += 1
        else:
            map[polymer[i: i + 2]] = 1

    counter = {}
    for l in polymer:
        if counter.get(l):
            counter[l] += 1
        else:
            counter[l] = 1

    steps = 40
    for step in range(1, steps + 1):
        new_map = {}
        for key, value in map.items():

            if counter.get(formulas[key]):
                counter[formulas[key]] += value
            else:
                counter[formulas[key]] = value

            if new_map.get(key[0] + formulas[key]):
                new_map[key[0] + formulas[key]] += value
            else:
                new_map[key[0] + formulas[key]] = value

            if new_map.get(formulas[key] + key[1]):
                new_map[formulas[key] + key[1]] += value
            else:
                new_map[formulas[key] + key[1]] = value

        map = new_map

    pprint(map)
    pprint(counter)

    return max(counter.values()) - min(counter.values())


if __name__ == "__main__":
    tic = time.perf_counter()
    r = main()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
