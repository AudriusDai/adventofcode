import time
from pprint import pprint

UNIQUE_FRAGMENTS = [2, 3, 4, 7]


def _is_1(fragment: str) -> bool:
    return len(fragment) == 2


def _is_4(fragment: str) -> bool:
    return len(fragment) == 4


def _is_7(fragment: str) -> bool:
    return len(fragment) == 3


def _is_8(fragment: str) -> bool:
    return len(fragment) == 7


def main() -> int:
    outputs = [line.split('|')[1].strip() for line in open('data.txt', 'r').readlines()]
    pprint(outputs)

    counter = 0
    for line in outputs:
        for fragment in line.split(' '):
            if len(fragment) in UNIQUE_FRAGMENTS:
                counter += 1

    return counter


if __name__ == "__main__":
    tic = time.perf_counter()
    r = main()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
