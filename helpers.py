from random import randint
from typing import List


def gen_descending_list(length: int, min_value: int = -10000, max_value: int = 10000) -> List[int]:
    asc_list = gen_ascending_list(length=length, min_value=min_value, max_value=max_value)
    return list(reversed(asc_list))


def gen_ascending_list(length: int, min_value: int = -10000, max_value: int = 10000) -> List[int]:
    return sorted([randint(min_value, max_value) for _ in range(length)])
