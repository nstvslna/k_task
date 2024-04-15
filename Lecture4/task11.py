def fibonacci_loop(seq):
    for num in seq:
        if isinstance(num, float):
            continue
        elif isinstance(num, str):
            break
        else:
            print(num, end=" ")


# Приклад
fibonacci_loop([0, 1, 1.1, 1, 2, 99.9, 3, 0.0, 5, 8, "stop", 13, 21, 34])
