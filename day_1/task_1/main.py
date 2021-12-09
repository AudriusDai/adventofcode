from day_1.task_1.data import DATA


def do_work():
    counter = 0
    for i in range(len(DATA)):
        if i == 0:
            continue

        if DATA[i] > DATA[i - 1]:
            counter += 1
    print(counter)


if __name__ == "__main__":
    do_work()
