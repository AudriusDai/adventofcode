from typing import List

from day_4.task_1.board import get_boards
from day_4.task_1.data import BOARDS, NUMBERS_PICKED
from day_4.task_1.roller import get_lucky_number


def do_work(raw_boards: List[List[List[int]]], numbers: List[int]) -> int:
    boards = get_boards(raw_boards)
    lucky_number, lucky_board = get_lucky_number(boards, numbers)
    unmarked_sum = lucky_board.get_unmarked_numbers_sum()

    return unmarked_sum * lucky_number


if __name__ == "__main__":
    r = do_work(BOARDS, NUMBERS_PICKED)
    print(f'Answer is: {r}')
