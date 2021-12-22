import math
import time
from typing import List


class ChunkStacker:
    def __init__(self):
        self.stack = []
        self.failed_on_signs = []
        self.missing_closed_signs = []

    def apply_chunk(self, chunk: str) -> None:
        for sign in chunk:
            if self._is_open_sing(sign):
                self.stack.append(sign)
            elif self._is_close_sing(sign) and not self.stack:
                print('got to closing sign, but there are none of open signs.. :(')
            elif self._is_close_sing(sign):
                last_open_sing = self.stack.pop()
                if not self._do_signs_match(last_open_sing, sign):
                    self.failed_on_signs.append(sign)
                    print(f'signs {last_open_sing} & {sign} do NOT match')
                    return

        if self.stack:
            print('some signs were not closed..')
            for i in range(len(self.stack)):
                last_sign = self.stack.pop()
                self.missing_closed_signs.append(self._get_closing_sing(last_sign))

            return

        print(f'all good with this chunk {chunk}!')

        return

    def has_chunk_failed(self) -> bool:
        return len(self.failed_on_signs) > 0

    def has_chunk_unclosed_signs(self) -> bool:
        return len(self.missing_closed_signs) > 0

    def _get_closing_sing(self, open_sign: str) -> str:
        if open_sign == '(':
            return ')'
        elif open_sign == '[':
            return ']'
        elif open_sign == '{':
            return '}'
        elif open_sign == '<':
            return '>'
        else:
            raise Exception(f'unknown open sign {open_sign}')

    def _is_open_sing(self, sign: str) -> bool:
        return sign in '([{<'

    def _is_close_sing(self, sign: str) -> bool:
        return sign in ')]}>'

    def _do_signs_match(self, open_sign: str, close_sign: str) -> bool:
        if open_sign == '(' and close_sign == ')':
            return True
        elif open_sign == '[' and close_sign == ']':
            return True
        elif open_sign == '{' and close_sign == '}':
            return True
        elif open_sign == '<' and close_sign == '>':
            return True
        else:
            return False


class IncompleteCounter:

    def __init__(self, signs: List[List[str]]):
        self.signs = signs

    def get_totals(self) -> List[int]:
        totals: List[int] = []
        for list_of_signs in self.signs:
            temp = 0
            for s in list_of_signs:
                temp = (temp * 5) + self._get_points(s)
            totals.append(temp)

        return totals

    def _get_points(self, sign: str) -> int:
        if sign == ')':
            return 1
        elif sign == ']':
            return 2
        elif sign == '}':
            return 3
        elif sign == '>':
            return 4
        else:
            raise Exception(f'unknown sign {sign}')


def main() -> int:
    incomplete_signs: List[List[str]] = []
    for chunk in [chunk.strip() for chunk in open('data.txt', 'r').readlines()]:
        c = ChunkStacker()
        c.apply_chunk(chunk)
        if c.has_chunk_unclosed_signs():
            print(f'chunk has missing close signs {c.missing_closed_signs}')
            incomplete_signs.append(c.missing_closed_signs)

    counter = IncompleteCounter(incomplete_signs)
    totals = counter.get_totals()
    totals.sort()
    print(totals)

    return totals[math.floor(len(totals) / 2)]


if __name__ == "__main__":
    tic = time.perf_counter()
    r = main()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
