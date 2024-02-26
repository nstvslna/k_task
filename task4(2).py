print("Введіть 3 числа:")
a = int(input())
b = int(input())
c = int(input())

max_num = a * (a > b and a > c) + b * (b > a and b > c) + c * (c > a and c > b)
min_num = a * (a < b and a < c) + b * (b < a and b < c) + c * (c < a and c < b)
mid_num = a * (min_num < a < max_num) + b * (min_num < b < max_num) + c * (min_num < c < max_num)

print("Результат:")
print(max_num)
print(min_num)
print(mid_num)
