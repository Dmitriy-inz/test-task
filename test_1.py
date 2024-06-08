from math import sqrt
from typing import Optional


def add_numbers(num_one: int, num_two: int) -> int:
    return num_one + num_two


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return

    user_perem = calculate_square_root(your_number)
    return f'Мы вычислили квадратный корень из введённого вами числа.\
 Это будет: {user_perem}'


num_user_1 = 10
num_user_2 = 5

print('Сумма чисел: ', add_numbers(num_user_1, num_user_2))

print(calc(25.5))
