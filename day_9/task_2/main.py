import time
from pprint import pprint


def get_uphill_coordinates(coordinates, field, collection):
    for coordinate in coordinates:
        collection.append(coordinate)
        coordinates_to_pass_forward = []
        x = coordinate[0]
        y = coordinate[1]
        value = field[x][y]

        left = field[x][y - 1] if y - 1 >= 0 else 9
        if left > value and left != 9:
            coordinates_to_pass_forward.append((x, y - 1))

        right = field[x][y + 1] if y + 1 < len(field[x]) else 9
        if right > value and right != 9:
            coordinates_to_pass_forward.append((x, y + 1))

        top = field[x - 1][y] if x - 1 >= 0 else 9
        if top > value and top != 9:
            coordinates_to_pass_forward.append((x - 1, y))

        bottom = field[x + 1][y] if x + 1 < len(field) else 9
        if bottom > value and bottom != 9:
            coordinates_to_pass_forward.append((x + 1, y))

        if coordinates_to_pass_forward:
            get_uphill_coordinates(coordinates_to_pass_forward, field, collection)

    return collection


def main() -> int:
    field = [[int(s) for s in line.strip()] for line in open('data.txt', 'r').readlines()]
    pprint(field)
    basins = []
    for x in range(len(field)):
        for y in range(len(field[0])):
            value = field[x][y]
            left = field[x][y - 1] if y - 1 >= 0 else 10
            right = field[x][y + 1] if y + 1 < len(field[x]) else 10
            top = field[x - 1][y] if x - 1 >= 0 else 10
            bottom = field[x + 1][y] if x + 1 < len(field) else 10
            if value < left and value < right and value < top and value < bottom:
                basins.append((x, y))

    enriched_basins = [get_uphill_coordinates([x], field, []) for x in basins]
    removed_duplicates = [list(set([i for i in x])) for x in enriched_basins]
    summed = [len(x) for x in removed_duplicates]
    summed.sort(reverse=True)
    result = summed[0] * summed[1] * summed[2]
    pprint(summed)
    return result


if __name__ == "__main__":
    tic = time.perf_counter()
    r = main()
    toc = time.perf_counter()
    print(f"It took {toc - tic:0.4f} seconds")
    print(f'Answer is: {r}')
