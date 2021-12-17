import time

from day_6.task_2.data_extractor import get_fish_numbers


def do_work():
    numbers = get_fish_numbers('data.txt')

    initial = {}
    initial[0] = numbers.count(0)
    initial[1] = numbers.count(1)
    initial[2] = numbers.count(2)
    initial[3] = numbers.count(3)
    initial[4] = numbers.count(4)
    initial[5] = numbers.count(5)
    initial[6] = numbers.count(6)
    initial[7] = numbers.count(7)
    initial[8] = numbers.count(8)
    temp = {}
    print(f'initial: {initial}')
    for i in range(256):
        temp[0] = initial[1]
        temp[1] = initial[2]
        temp[2] = initial[3]
        temp[3] = initial[4]
        temp[4] = initial[5]
        temp[5] = initial[6]
        temp[6] = initial[7]
        temp[7] = initial[8]

        temp[6] += initial[0]
        temp[8] = initial[0]
        initial = temp
        temp = {}
        print(f'day {i + 1}: {initial}')

    return sum([x for x in initial.values()])


if __name__ == "__main__":
    tic = time.perf_counter()
    r = do_work()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
