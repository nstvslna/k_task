def sum_of_odd_digits(n):
    if not isinstance(n, int) or n < 0:
        raise TypeError("n must be a non-negative integer")

    sum_odd_digits = 0
    n_str = str(n)

    for digit_str in n_str:
        digit = int(digit_str)
        if digit % 2 != 0:
            sum_odd_digits += digit

    return sum_odd_digits


print(sum_of_odd_digits(1234))
print(sum_of_odd_digits(246))
