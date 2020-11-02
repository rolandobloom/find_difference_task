import re

from method import find_difference

if __name__ == '__main__':
    array_a = list(map(int, re.findall(r'[^,\.\s]+', input('enter array A:'))))
    array_b = list(map(int, re.findall(r'[^,\.\s]+', input('enter array B:'))))

    result = find_difference(array_a, array_b)

    print(f'Min difference: {result}')
