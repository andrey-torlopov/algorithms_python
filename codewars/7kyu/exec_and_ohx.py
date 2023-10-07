# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    d = {'X': 0, 'O': 0}
    for i in s:
        letter = i.upper()
        if letter == 'X' or letter == 'O':
            d[letter] += 1
    return d['X'] == d['O']