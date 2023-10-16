# Данн отсортированный массив
# [-4, -3, -1, 0, 2, 6, 8, 9, 10]
# Написать метод, который примет на вход массив
# и вернет массив с возведенными элементами в квадрат
#  также отсортированными.

import time


def square_list(array):
    res = []
    l, r = 0, len(array) - 1

    while l <= r:
        time.sleep(2)
        print(array)
        print(f"l = {l}, r = {r}")
        print(f"res = {res}")
        print("*" * 50)

        if abs(array[l]) > abs(array[r]):
            res.append(array[l] ** 2)
            l += 1
        else:
            res.append(array[r] ** 2)
            r -= 1
    return res[::-1]


a = [-4, -3, -2, 0, 0, 2, 3, 5]
r = square_list(a)

print(r)
