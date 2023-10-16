# Suppose we know the process by which a string s was encoded
# to a string r (see explanation below). The aim of the kata
# is to decode this string r to get back the original string s.

# Explanation of the encoding process:

# input: a string s composed of lowercase letters from "a" to "z", and a positive integer num
# we know there is a correspondence between abcde...uvwxyzand 0, 1, 2 ..., 23, 24, 25 : 0 <-> a, 1 <-> b ...
# if c is a character of s whose corresponding number is x, apply to x the function f: x-> f(x) = num * x % 26, then find ch the corresponding character of f(x)
# Accumulate all these ch in a string r
# concatenate num and r and return the result

# encode("mer", 6015)  -->  "6015ekx"

# m --> 12,   12 * 6015 % 26 = 4,    4  --> e
# e --> 4,     4 * 6015 % 26 = 10,   10 --> k
# r --> 17,   17 * 6015 % 26 = 23,   23 --> x

# So we get "ekx", hence the output is "6015ekx"

# decode "6015ekx" -> "mer"
# decode "5057aan" -> "Impossible to decode"


def parse_num_string(s) -> (int, str):
    num = ""
    for char in s:
        if char.isdigit():
            num += char
        else:
            break
    return int(num), s[len(num):]


def decode(r):
    num, r = parse_num_string(r)
    keys = {}
    for i in range(26):
        letter = ord('a') + i
        keys[chr(ord('a') + i * num % 26)] = chr(letter)
    if len(keys) != 26:
        return "Impossible to decode"
    return ''.join([keys[char] for char in list(r)])
