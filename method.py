from sys import maxsize
from typing import List


def find_difference(array_a: List[int], array_b: List[int]) -> int:
    result = maxsize

    b = 0
    n = len(array_b)

    array_a = reversed(array_a)
    a_element = next(array_a)
    while b < n:
        if abs(a_element - array_b[b]) < result:
            result = abs(a_element - array_b[b])

        if a_element < array_b[b]:
            try:
                a_element = next(array_a)
            except StopIteration:
                break
        elif a_element > array_b[b]:
            b += 1
        else:
            break

    return result
