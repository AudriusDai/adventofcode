import time
from pprint import pprint
from typing import List, Tuple


def main() -> int:
    polymer = 'KKOSPHCNOCHHHSPOBKVF'
    values: List[List[str]] = [line.strip().split(' -> ') for line in open('data.txt', 'r').readlines()]
    formulas = {v[0]: v[1] for v in values}

    steps = 10
    for step in range(1, steps + 1):
        temp_polymer = polymer[0]

        for i in range(len(polymer) - 1):
            bit = polymer[i: i + 2]
            temp_polymer += formulas[bit] + polymer[i + 1]

        polymer = temp_polymer

    letters = set(formulas.values())

    counts = [polymer.count(letter) for letter in letters]
    return max(counts) - min(counts)


if __name__ == "__main__":
    tic = time.perf_counter()
    r = main()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
