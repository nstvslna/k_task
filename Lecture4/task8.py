def get_pairs(elements):
    if len(elements) <= 1:
        return None

    pairs = []
    for i in range(len(elements) - 1):
        current_element = elements[i]
        next_element = elements[i + 1]
        pair = (current_element, next_element)
        pairs.append(pair)

    return pairs


print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1]))
