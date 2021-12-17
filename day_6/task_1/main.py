from day_6.task_1.data_extractor import get_fish_numbers
from day_6.task_1.fish import grow_fish
import time


def do_work() -> int:
    initial_fish_numbers = get_fish_numbers('data_2.txt')
    final_fish_list = grow_fish(initial_fish_numbers, 110)

    return len(final_fish_list)


if __name__ == "__main__":
    tic = time.perf_counter()
    r = do_work()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
