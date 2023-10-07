# Complete the function scramble(str1, str2) that returns
# true if a portion of str1 characters can be rearranged
# to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.

# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

def scramble(s1, s2) -> bool:
    if len(s1) < len(s2):
        return False
    letters = [0 for i in range(26)]

    for i in range(len(s1)):
        letters[ord(s1[i]) - 97 - 1] += 1
        if i < len(s2):
            letters[ord(s2[i]) - 97 - 1] -= 1

    return len(list(filter(lambda x: x < 0, letters))) == 0


print(scramble('rkqodlw', 'world'))
# print(scramble('cedewaraaossoqqyt', 'codewars'))
# print(scramble('katas', 'steak'))
