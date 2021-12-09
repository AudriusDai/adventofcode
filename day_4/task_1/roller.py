from typing import List

from day_4.task_1.board import Board


def get_lucky_number(boards: List[Board], numbers: List[int]) -> (int, Board):
    n = 0
    b = None
    for number in numbers:
        for board in boards:
            was_marked = board.try_mark_number(number)
            if was_marked and board.has_bingo():
                n = number
                b = board
        if n != 0:
            break

    return n, b
