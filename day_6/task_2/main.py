import asyncio
from multiprocessing import Pool
import time

from day_6.task_2.data_extractor import get_fish_numbers, chop_fish_numbers
from day_6.task_2.fish import fish_wrapper, fish_wrapper_2, fish_wrapper_3


def flatten(t):
    return [item for sublist in t for item in sublist]


async def do_work():
    file_names = chop_fish_numbers(chunk_size=5, file_name='data_2.txt')
    final = 0
    for name in file_names:
        fish_list = get_fish_numbers(name)
        with Pool(processes=5) as pool:
            results = pool.map(fish_wrapper, fish_list, 1)
            results = flatten(results)
            f = open(f"results/{name.split('/')[1]}", "w")
            f.write(",".join([str(x) for x in results]))
            f.close()
            r = len(results)
            final += r
            print(f'File {name} handled: {r}')

    return final


if __name__ == "__main__":
    tic = time.perf_counter()
    r = asyncio.run(do_work())
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
