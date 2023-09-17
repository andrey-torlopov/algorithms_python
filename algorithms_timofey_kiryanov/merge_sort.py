# Сортировка слиянием
import time


def merge(a: list, b: list) -> list:
    """Слияние двух отсортированных списков"""

    if len(a) == 0:
        return b

    if len(b) == 0:
        return a

    i, j, c = 0, 0, []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i < len(a):
        c.extend(a[i:])
    if j < len(b):
        c.extend(b[j:])

    return c


def merge_sort(a: list) -> list:
    """Сортировка слиянием"""
    if len(a) <= 1:
        return a
    middle = len(a) // 2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])
    return merge(left, right)


# random_array = [1, 5, 3, 6, 8, 4, 2, 9, 7]
# print(merge_sort(random_array))
