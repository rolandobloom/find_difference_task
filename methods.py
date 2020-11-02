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
