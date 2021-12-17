import time


def main() -> int:
    positions = [int(x) for x in open('data.txt', 'r').readline().split(',')]
    fuels = []
    for x in range(min(positions), max(positions)):
        fuels.append(sum([abs(x - p) for p in positions]))

    print(fuels)
    return min(fuels)


if __name__ == "__main__":
    tic = time.perf_counter()
    r = main()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
