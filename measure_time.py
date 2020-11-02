import timeit

from helpers import gen_ascending_list, gen_descending_list
from methods import Approach

array_a = gen_descending_list(length=1000, min_value=-1000, max_value=1000)
array_b = gen_ascending_list(length=1000, min_value=0, max_value=1000)

NUMBER_OF_REPEATS = 5
NUMBER_OF_LOOPS = 1000


def time_it(approach: str, early: bool = False) -> None:
    setup = (
        f'from methods import {approach}, check_for_early_result\n'
        'from measure_time import array_a, array_b\n'
    )

    if early:
        setup += f'test_method = check_for_early_result({approach}.find_difference)'
    else:
        setup += f'test_method = {approach}.find_difference'

    timer = timeit.Timer('test_method(array_a, array_b)', setup=setup)
    result = timer.repeat(repeat=NUMBER_OF_REPEATS, number=NUMBER_OF_LOOPS)

    print(f'{NUMBER_OF_LOOPS} loops, best of {NUMBER_OF_REPEATS}: {min(result)} per loop \n')


if __name__ == '__main__':
    approaches = Approach.get_subclasses_names()
    for a in approaches:
        print(f'Testing approach "{a}":')
        time_it(a)
        print(f'with early checking:')
        time_it(a, early=True)
