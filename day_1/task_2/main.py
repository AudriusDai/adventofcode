from day_1.task_2.analyzer.analyzer import get_count_of_greater_than_previous
from day_1.task_2.data import DATA
from day_1.task_2.grouper.grouper import group_data


def do_work(data) -> int:
    print(f'  data: {data}')
    grouped = group_data(data, 3)
    print(f'  grouped: {grouped}')
    greater = get_count_of_greater_than_previous(grouped)
    print(f'  greater: {greater}')
    return greater


if __name__ == "__main__":
    r = do_work(DATA)
    print(f'Answer is: {r}')
