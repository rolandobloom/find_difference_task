from abc import ABC, abstractmethod
from sys import maxsize
from typing import List


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
            if abs(array_a[a] - array_b[b]) < result:
                result = abs(array_a[a] - array_b[b])

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
            if abs(array_a[a] - array_b[b]) < result:
                result = abs(array_a[a] - array_b[b])

            if array_a[a] < array_b[b]:
                a -= 1
            elif array_a[a] > array_b[b]:
                b += 1
            else:
                break

        return result
