def min_distance_to_border(N, M, x, y):
    min_distance_to_short_border = min(y, M - y)
    min_distance_to_long_border = min(x, N - x)
    return min(min_distance_to_short_border, min_distance_to_long_border)


print("Введіть розмір басейну у форматі N на M: ")
# Зчитуємо вхідні дані
N, M = int(input()), int(input())
x = int(input("Введіть відстань,на якій ви знаходитеся від одного з довгих бортиків: "))
y = int(input("Введіть відстань,на якій ви знаходитеся від одного з коротких бортиків: "))
print(min_distance_to_border(N, M, x, y))
