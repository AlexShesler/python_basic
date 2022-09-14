"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda x: x ** 2, numbers))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number: int) -> bool:
    if number in (0, 1) or (number % 2 == 0 and number != 2):
        return False
    div = 3
    while div * div <= number and number % div != 0:
        div += 2
    return div * div > number


def filter_numbers(numbers_list: list, filter_type: str) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == "odd":
        return list(filter(lambda x: x % 2 != 0, numbers_list))
    if filter_type == "even":
        return list(filter(lambda x: x % 2 == 0, numbers_list))
    if filter_type == "prime":
        return list(filter(lambda x: is_prime(x), numbers_list))
