# Define a function that takes in two non-negative integers a and b
# and returns the last decimal digit of a^b. Note that a and b may be very large!

# 9^7 = 4782969
# 0^0 = 1
# last_digit(4, 1)                # returns 4
# last_digit(4, 2)                # returns 6
# last_digit(9, 7)                # returns 9
# last_digit(10, 10 ** 10)        # returns 0
# last_digit(2 ** 200, 2 ** 300)  # returns 6

def last_digit(n1, n2) -> int:
    if n2 == 0:
        return 1
    numb = int(str(n1)[-1])
    pow_value = n2 % 4
    if pow_value == 0:
        pow_value = 4
    return int(str(numb ** pow_value)[-1])
