# 1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246. Squaring these divisors
# we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681. The sum of
# these squares is 84100 which is 290 * 290.

# Task

# Find all integers between m and n (m and n integers with 1 <= m <= n) such that
# the sum of their squared divisors is itself a square.

# We will return an array of subarrays or of tuples (in C an array of Pair) or a string.
# The subarrays (or tuples or Pairs) will have two elements: first the number the squared
# divisors of which is a square and then the sum of the squared divisors.

# list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
# list_squared(42, 250) --> [[42, 2500], [246, 84100]]

# The form of the examples may change according to the language, see "Sample Tests".

# Note

# In Fortran - as in any other language - the returned string is not permitted
# to contain any redundant trailing whitespace: you can use dynamically
# allocated character strings.

def find_divisors(numb: int) -> list[int]:
    return [i for i in range(1, numb + 1) if numb % i == 0]


def find_divisors2(number) -> list[int]:
    divisors = set()

    # Итерируемся только до квадратного корня числа (округленного до ближайшего целого)
    sqrt_num = int(number ** 0.5) + 1

    for i in range(1, sqrt_num):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)  # Добавляем также "парный" делитель

    # Если число само не равно 1, то оно также является своим делителем
    if number != 1:
        divisors.add(number)

    return list(divisors)


def list_squared(m, n) -> list[int]:
    result = []
    for numb in range(m, n + 1):
        deviders = find_divisors(numb)
        square_sum = sum([i ** 2 for i in deviders])
        if square_sum ** 0.5 % 1 == 0:
            result.append([numb, square_sum])
    return result
