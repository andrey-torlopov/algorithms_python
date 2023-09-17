# Сортировака методом Том Хоара

def hoar_sort(a: list) -> list:
    if len(a) <= 1:
        return a

    barriar = a[0]
    left = []
    right = []
    middle = []
    for x in a:
        if x < barriar:
            left.append(x)
        elif x == barriar:
            middle.append(x)
        else:
            right.append(x)
    k = 0
    left = hoar_sort(left)
    right = hoar_sort(right)
    for x in left + middle + right:
        a[k] = x
        k += 1

    return a


def check_sorted(a: list, ascending: bool = True) -> bool:
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, len(a) - 2):
        if s * a[i] > s * a[i + 1]:
            flag = False
            break
    return flag


a = [1, 2, 3, 4, 6]
print(check_sorted(a))
