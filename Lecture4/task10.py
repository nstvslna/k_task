def sum_binary_1(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    binary_str = bin(n)[2:]
    ones_count = binary_str.count('1')

    return ones_count


# Приклади використання
print(sum_binary_1(14))  # 3
print(sum_binary_1(128))  # 1
