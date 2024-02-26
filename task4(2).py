print("Введіть 3 числа:")
a = int(input())
b = int(input())
c = int(input())

max_num = (a >= b) * a + (b > a) * b
max_num = (max_num >= c) * max_num + (c > max_num) * c

min_num = (a <= b) * a + (b < a) * b
min_num = (min_num <= c) * min_num + (c < min_num) * c

mid_num = (a + b + c) - max_num - min_num

print("Результат:")
print(max_num)
print(min_num)
print(mid_num)
