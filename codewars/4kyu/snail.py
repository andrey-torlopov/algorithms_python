# Snail Sort

# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:

def get_column(array: list[list[int]], index: int) -> list[int]:
    column = []
    for row in array:
        column.append(row[index])

    return column


def remove_column(array: list[list[int]], index: int) -> list[list[int]]:
    for row in array:
        row.pop(index)
    return array


def snail(snail_map: list[list[int]]) -> list[int]:
    array = snail_map
    result = []
    state = 0  # 0: right, 1: down, 2: left, 3: up
    while len(array) > 0:
        if state == 0:
            result += array.pop(0)
            state = 1
        elif state == 1:
            result += get_column(array, -1)
            array = remove_column(array, -1)
            state = 2
        elif state == 2:
            result += array.pop(-1)[::-1]
            state = 3
        elif state == 3:
            result += get_column(array, 0)[::-1]
            array = remove_column(array, 0)
            state = 0
    return result


def snail2(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1]  # Rotate
    return out


# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
