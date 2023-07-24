# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(text, ending):
    return text[-len(ending):] == ending
    