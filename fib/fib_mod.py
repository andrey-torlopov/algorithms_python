# Задача:
# Даны целые числа 1 <= n <= 10^18 и 2 <= m <= 10^5, необходимо найти остаток от деления n-го числа Фибоначчи на m.
# Sample Input:
# 10 2
# Sample Output:
# 1
# Memory Limit: 256 MB
# Time Limit: 5 seconds

def get_pisano_period(m):
    a, b = 0, 1
    period = 0
    for _ in range(m * m):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            return period + 1
        period += 1

def fib_mod(n, m):
    pisano_period = get_pisano_period(m)
    n = n % pisano_period

    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % m

    return b


result = fib_mod(10, 2)
print(result)