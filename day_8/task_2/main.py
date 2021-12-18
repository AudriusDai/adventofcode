import time
from pprint import pprint


class DigitalNumber:
    def __init__(self, input: str, output: str):
        self.output = output
        self.num_map = self._get_num_map(input)

    def get_output_number(self):
        num_str = ''
        for fragment in self.output.split(' '):
            num_str += str(self._get_number(fragment))
        return int(num_str)

    def _are_all_letters_in(self, letters, word):
        if not letters:
            return False

        for letter in letters:
            if letter not in word:
                return False

        return True

    def _has_3_same_letters(self, letters, word):
        if not letters:
            return False
        counter = 0
        for letter in letters:
            if letter in word:
                counter += 1

        return counter == 3

    def _get_num_map(self, input: str) -> dict:
        num_map = {str(x): '' for x in range(10)}
        number_for_second_chance = []
        for f in input.split(' '):
            # set the known unique size numbers
            if len(f) == 2:
                num_map['1'] = f
            elif len(f) == 4:
                num_map['4'] = f
            elif len(f) == 3:
                num_map['7'] = f
            elif len(f) == 7:
                num_map['8'] = f

        for f in input.split(' '):
            if len(f) == 6:
                # figure out the 0, 6 or 9
                if self._are_all_letters_in(num_map['4'], f):
                    num_map['9'] = f
                    continue
                if num_map['9'] and self._are_all_letters_in(num_map['7'], f):
                    num_map['0'] = f
                    continue
                # if not found yet, let's add for later
                number_for_second_chance.append(f)
                continue

            if len(f) == 5:
                # figure out the 2, 3 or 5
                if self._are_all_letters_in(num_map['1'], f):
                    num_map['3'] = f
                    continue
                if self._has_3_same_letters(num_map['4'], f):
                    num_map['5'] = f
                    continue
                # if not found yet, let's add for later
                number_for_second_chance.append(f)
                continue

        for second_time in number_for_second_chance:
            if len(second_time) == 6:
                # figure out the 0 or 6
                if self._has_3_same_letters(num_map['7'], second_time):
                    num_map['0'] = second_time
                else:
                    num_map['6'] = second_time
                continue
            if len(second_time) == 5:
                # figure out the 2 or 5
                if self._has_3_same_letters(num_map['4'], second_time):
                    num_map['5'] = second_time
                else:
                    num_map['2'] = second_time
                continue

        return num_map

    def _get_number(self, fragment: str) -> int:

        for key, value in self.num_map.items():
            if len(value) != len(fragment):
                continue

            good = True
            for letter in fragment:
                if letter not in value:
                    good = False

            if not good:
                continue

            return key


def main() -> int:
    lines = [{'input': line.split('|')[0].strip(), 'output': line.split('|')[1].strip()} for line in
             open('data.txt', 'r').readlines()]
    pprint(lines)

    counter = []
    for line in lines:
        n = DigitalNumber(line['input'], line['output'])
        counter.append(n.get_output_number())

    pprint(counter)
    return sum(counter)


if __name__ == "__main__":
    tic = time.perf_counter()
    r = main()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
