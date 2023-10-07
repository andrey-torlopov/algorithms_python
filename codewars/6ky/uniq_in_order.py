# Implement the function unique_in_order which takes as argument a sequence and returns
# a list of items without any elements with the same value next to each other and
# preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence: str) -> list[str]:
    if len(sequence) == 0:
        return []
    result = [sequence[0]]
    for index in range(1, len(sequence)):
        if sequence[index] != sequence[index - 1]:
            result.append(sequence[index])

    return result


def unique_in_order_2(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res


print(unique_in_order((1, 2, 2, 3, 3)))
