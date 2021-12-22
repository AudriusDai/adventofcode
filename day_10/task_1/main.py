import time
from typing import List


class ChunkStacker:
    def __init__(self):
        self.stack = []
        self.failed_on_signs = []

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

        print(f'all good with this chunk {chunk}!')

        return

    def has_chunk_failed(self) -> bool:
        return len(self.failed_on_signs) > 0

    def _is_open_sing(self, sign: str) -> bool:
        return sign in '([{<'

    def _is_close_sing(self, sign: str) -> bool:
        return sign in ')]}>'

    def _do_signs_match(self, open_sing: str, close_sign: str) -> bool:
        if open_sing == '(' and close_sign == ')':
            return True
        elif open_sing == '[' and close_sign == ']':
            return True
        elif open_sing == '{' and close_sign == '}':
            return True
        elif open_sing == '<' and close_sign == '>':
            return True
        else:
            return False


class IllegalCounter:

    def __init__(self, illegal_signs: List[str]):
        self.signs = illegal_signs

    def get_total(self) -> int:
        return sum([self._get_points(s) for s in self.signs])

    def _get_points(self, sign: str) -> int:
        if sign == ')':
            return 3
        elif sign == ']':
            return 57
        elif sign == '}':
            return 1197
        elif sign == '>':
            return 25137
        else:
            raise Exception(f'unknown sign {sign}')


def main() -> int:
    illegal_signs = []
    for chunk in [chunk.strip() for chunk in open('data.txt', 'r').readlines()]:
        c = ChunkStacker()
        c.apply_chunk(chunk)
        if c.has_chunk_failed():
            print(f'chunk has failed on illegal {c.failed_on_signs[0]} sign')
            illegal_signs.append(c.failed_on_signs[0])

    counter = IllegalCounter(illegal_signs)

    return counter.get_total()


if __name__ == "__main__":
    tic = time.perf_counter()
    r = main()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
