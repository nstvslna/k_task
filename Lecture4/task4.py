from typing import List


def split_by_index(string: str, indexes: List[int]) -> List[str]:
    result = []
    prev_index = 0

    for index in indexes:
        # Ігноруємо недопустимі індекси
        if not isinstance(index, int) or index <= prev_index or index >= len(string):
            continue

        result.append(string[prev_index:index])
        prev_index = index

    # Додаємо останній фрагмент
    result.append(string[prev_index:])

    return result


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18]))
print(split_by_index("no luck", [42]))
