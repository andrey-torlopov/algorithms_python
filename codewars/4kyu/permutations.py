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


# Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

import functools
import itertools
import time


def permutations2(string):
    return sorted(list("".join(p) for p in set(itertools.permutations(string))))


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
    return sorted(list(set(permutations)))


input_string = "ABAB"
all_permutations = permutations(input_string)
b = sorted(all_permutations)
print(b)


@functools.lru_cache(maxsize=None)
def permutations3(string):
    string = sorted(string)
    permutations_list = []
    permutations_list.append(''.join(string))

    while True:
        next_perm = next_permutation(string)
        if next_perm == string:
            break
        permutations_list.append(''.join(next_perm))

    return permutations_list


def list_positin(word):
    sorted_words = permutations(word)

    print(word)
    try:
        return sorted_words.index(word) + 1
    except ValueError:
        return 1


input_string = "ABAB"
result = list_positin(input_string)
print(result)
