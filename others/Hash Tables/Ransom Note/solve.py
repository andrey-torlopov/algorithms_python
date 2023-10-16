from functools import reduce

magazine = "apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg".split()
note = "elo lxkvg bg mwz clm w".split()

def checkMagazine(magazine, note):
  words = {}
  for word in note:
      words[word] = words.get(word,0) + 1

  for word in magazine:
    if words.get(word, None) != None and words[word] > 0:
      words[word] -= 1

  print(words)
  result = reduce(lambda res, word: res + words[word], words, 0)
  print("Yes" if result == 0 else "No")

checkMagazine(magazine, note)