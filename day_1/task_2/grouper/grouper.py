from typing import List


def group_data(data: List[int], group_size: int) -> List[int]:
    result = []
    if not data:
        return result

    if len(data) < group_size:
        raise Exception(f'group size cannot be greater than data provided: data: {len(data)}, group_size: {group_size}')

    for i in range(len(data) - (group_size - 1)):
        s = 0
        for j in range(group_size):
            s += data[i + j]
        result.append(s)

    return result
