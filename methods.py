from abc import ABC, abstractmethod
from sys import maxsize
from typing import Callable, List, Optional


# If lists has no intersecting range, we do not need to check every element
def check_for_early_result(function: Callable):
    def wrapper(array_a: List[int], array_b: List[int]) -> Callable:
        def get_early_result() -> Optional[int]:
            a_first = array_a[0]
            a_last = array_a[-1]
            b_first = array_b[0]
            b_last = array_b[-1]

            if a_first <= b_first:
                return abs(b_first - a_first)
            if a_last >= b_last:
                return abs(a_last - b_last)

        early_result = get_early_result()
        return early_result or function(array_a, array_b)

    return wrapper


class Approach(ABC):
    @staticmethod
    @abstractmethod
    def find_difference(array_a: List[int], array_b: List[int]) -> int:
        """
        :param array_a: descending sorted list of integers
        :param array_b: ascending sorted list of integers
        :return: minimum absolute difference between two elements of two lists
        """
        raise NotImplementedError

    @classmethod
    def get_subclasses_names(cls) -> List[str]:
        return [subclass.__name__ for subclass in cls.__subclasses__()]


class ReverseWithReversed(Approach):
    @staticmethod
    def find_difference(array_a: List[int], array_b: List[int]) -> int:
        result = maxsize

        b = 0
        n = len(array_b)

        array_a = reversed(array_a)
        a_element = next(array_a)
        while b < n:
            if (_result := abs(a_element - array_b[b])) < result:
                result = _result

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


class ReverseWithSlice(Approach):
    @staticmethod
    def find_difference(array_a: List[int], array_b: List[int]) -> int:
        result = maxsize

        a = 0
        b = 0

        array_a = array_a[::-1]

        m = len(array_a)
        n = len(array_b)
        while a < m and b < n:
            if (_result := abs(array_a[a] - array_b[b])) < result:
                result = _result

            if array_a[a] < array_b[b]:
                a += 1
            elif array_a[a] > array_b[b]:
                b += 1
            else:
                break

        return result


class GoBackwards(Approach):
    @staticmethod
    def find_difference(array_a: List[int], array_b: List[int]) -> int:
        result = maxsize

        a = len(array_a) - 1
        b = 0

        n = len(array_b)
        while a >= 0 and b < n:
            if (_result := abs(array_a[a] - array_b[b])) < result:
                result = _result

            if array_a[a] < array_b[b]:
                a -= 1
            elif array_a[a] > array_b[b]:
                b += 1
            else:
                break

        return result
