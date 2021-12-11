from day_5.task_1.data_extractor import get_vectors
from day_5.task_1.field import Field


def do_work() -> int:
    vectors = [v for v in get_vectors('data.txt') if not v.is_diagonal()]
    f = Field()
    for v in vectors:
        f.apply_vector(v)

    r = f.get_dangerous_points_count()
    return r


if __name__ == "__main__":
    r = do_work()
    print(f'Answer is: {r}')
