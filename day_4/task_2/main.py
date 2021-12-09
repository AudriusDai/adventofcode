from typing import List

from day_4.task_2.board import get_boards
from day_4.task_2.data import BOARDS, NUMBERS
from day_4.task_2.roller import get_lucky_number


def do_work(raw_boards: List[List[List[int]]], numbers: List[int]) -> int:
    boards = get_boards(raw_boards)
    lucky_number, last_board = get_lucky_number(boards, numbers)
    unmarked_sum = last_board.get_unmarked_numbers_sum()

    return unmarked_sum * lucky_number


if __name__ == "__main__":
    r = do_work(BOARDS, NUMBERS)
    print(f'Answer is: {r}')
