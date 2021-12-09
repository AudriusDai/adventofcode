from typing import List


class Board:
    rows: List[List[int]]
    columns: List[List[int]]
    marked_numbers: List[int]

    def __init__(self):
        self.rows = []
        self.columns = []
        self.marked_numbers = []

    def add_row(self, row: List[int]):
        self.rows.append(row)

    def add_column(self, column: List[int]):
        self.columns.append(column)

    def try_mark_number(self, number: int) -> bool:
        marked = False
        for row in self.rows:
            if number in row:
                row.remove(number)
                marked = True
                self.marked_numbers.append(number)
                break

        for column in self.columns:
            if number in column:
                column.remove(number)
                if not marked:
                    self.marked_numbers.append(number)
                marked = True
                break

        return marked

    def has_bingo(self) -> bool:
        bingo = False
        for r in self.rows:
            if not r:
                bingo = True
                break

        for c in self.columns:
            if not c:
                bingo = True
                break

        return bingo

    def get_unmarked_numbers_sum(self) -> int:
        return sum([sum(r) for r in self.rows])


def get_boards(raw_boards: List[List[List[int]]]) -> List[Board]:
    l: List[Board] = []

    for raw_board in raw_boards:
        b = Board()
        for row in raw_board:
            b.add_row(row)

        for column_index in range(len(raw_board[0])):
            column: List[int] = []
            for row_item in range(len(raw_board)):
                column.append(raw_board[row_item][column_index])
            b.add_column(column)

        l.append(b)

    return l
