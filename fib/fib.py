# Вычислить ряд Фибоначчи
arr = [1, 1, 2]
def fib(n):
    if n <= 3:
        return arr[n-1]
    for i in range(3, n):
        arr.append(arr[i-1] + arr[i-2])
    return arr[n-1]
    
        
print(fib(3))
