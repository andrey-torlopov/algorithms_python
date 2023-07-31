# In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.
# Create as many "shufflings" as you can!
# Examples:
# With input 'a':
# Your function should return: ['a']

# With input 'ab':
# Your function should return ['ab', 'ba']

# With input 'abc':
# Your function should return ['abc','acb','bac','bca','cab','cba']

# With input 'aabb':

'''
a1 -> a2 b1 b2:
 a2 b1 b2 a1
 a2 b1 a1 b2
 a2 a1 b1 b2
 a1 a2 b1 b2
 
a2 -> a1 b1 b2:
 a1 b1 b2 a2
 a1 b1 a2 b2
 a1 a2 b1 b2
 a2 a1 b1 b2

b1 -> a1 a2 b2:
 a1 a2 b2 b1
 a1 a2 b1 b2
 a1 b1 a2 b2
 b1 a1 a2 b2

b2 -> a1 a2 b1:
 a1 a2 b1 b2
 a1 a2 b2 b1
 a1 b2 a2 b1
 b2 a1 a2 b1
 
SUM:
 
'''

# Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

import itertools


def permutations2(string):
    return list("".join(p) for p in set(itertools.permutations(string)))


def permutations(s: str) -> list[str]:
    def generate_permutations(prefix, remaining) -> None:
        if len(remaining) == 0:
            permutations.append(prefix)
        else:
            for i in range(len(remaining)):
                new_prefix = prefix + remaining[i]
                new_remaining = remaining[:i] + remaining[i + 1:]
                generate_permutations(new_prefix, new_remaining)

    permutations = []
    generate_permutations("", s)
    return list(set(permutations))


# Пример использования:
input_string = "abc"
all_permutations = permutations(input_string)
for permutation in all_permutations:
    print(permutation)
