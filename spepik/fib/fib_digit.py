# Получить последнее число Фибоначчи для n-го числа

fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

fib_a = None
fib_b = None

def fib_digit(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    fib_a = 1
    fib_b = 1
    
    for i in range(2, n):
        fib_c = fib_a + fib_b
        fib_a = fib_b
        fib_b = fib_c
    
    return fib_c % 10

arr = [1, 1, 2]
def fib(n):
    if n <= 3:
        return arr[n-1]
    for i in range(3, n):
        arr.append((arr[i-1] + arr[i-2]) % 10)
    return arr[n-1]

        
print(fib(841645))