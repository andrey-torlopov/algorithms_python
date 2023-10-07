def count_bits(n):
    # return len(list(filter(lambda x: x == '1', list(str(bin(a)[2:])))))
    return bin(n).count('1')