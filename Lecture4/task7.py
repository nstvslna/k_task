from typing import List


def foo(nums: List[int]) -> List[int]:
    result = []

    # Знаходимо добуток всіх чисел у вихідному списку
    product = 1
    for num in nums:
        product *= num

    # Заповнюємо список результатів, діленням добутку на кожне число
    for num in nums:
        result.append(product // num)

    return result


# Приклади
print(foo([1, 2, 3, 4, 5]))
print(foo([3, 2, 1]))
