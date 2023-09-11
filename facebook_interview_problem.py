# Есть массив
# [4, 2, 2, 1, 2, -3, 5, -8] найти сколькими способами можно получить 5
# например [2 + 2 + 1], [1 + 2 + -3 + 5] итп
import time


def count_sum(array, sum):
    d = {0: 1}
    for_sum = 0
    result = 0

    for item in array:
        for_sum += item
        diff = for_sum - sum

        if for_sum == sum:
            d[for_sum] = d.get(for_sum, 0) + 1
            result += 1
        elif diff in d:
            result += d.get(diff, 0)
            d[for_sum] = d.get(for_sum, 0) + 1
        else:
            d[for_sum] = d.get(for_sum, 0) + 1

        print(f"item = {item} for_sum = {for_sum} result = {result} d = {d}")

    return result


arr = [5, 0, 0, 0]
# arr = [4, 2, 2, 1, 2, -3, 5, -8]
print(count_sum(arr, 5))
