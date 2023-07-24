def get_count(sentence):
    result = 0
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    for i in sentence:
        if i in vowels:
            result += 1
    return result
