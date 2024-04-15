from typing import Tuple


def get_digits(*args: int) -> Tuple[int]:
    digits = tuple(int(digit) for num in args for digit in str(num))
    return digits


# Приклад використання
print(get_digits(8717, 82911, 99))
