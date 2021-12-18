import time
from pprint import pprint


def main() -> int:
    field = [[int(s) for s in line.strip()] for line in open('data.txt', 'r').readlines()]
    pprint(field)
    risk_levels = []
    for x in range(len(field)):
        for y in range(len(field[0])):
            value = field[x][y]
            left = field[x][y - 1] if y - 1 >= 0 else 10
            right = field[x][y + 1] if y + 1 < len(field[x]) else 10
            top = field[x - 1][y] if x - 1 >= 0 else 10
            bottom = field[x + 1][y] if x + 1 < len(field) else 10
            if value < left and value < right and value < top and value < bottom:
                risk_levels.append(value + 1)

    pprint(risk_levels)
    return sum(risk_levels)


if __name__ == "__main__":
    tic = time.perf_counter()
    r = main()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
