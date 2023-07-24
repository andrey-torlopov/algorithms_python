def narcissistic(value):
    numbers = [int(i) for i in str(value)]
    p = len(numbers)
    result = 0
    for i in numbers:
        result += i ** p
    
    return result == value