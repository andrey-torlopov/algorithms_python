import string

signatures = {}
ALPHABET = string.ascii_lowercase
signature = [0 for _ in ALPHABET]

for letter in s:
  signature[ord(letter)-ord(ALPHABET[0])] += 1

# iterate over all substrings of s
for start in range(len(s)):
  for finish in range(start, len(s)):
    # initialize substring signature
    signature = [0 for _ in ALPHABET]
    for letter in s[start:finish+1]:
      signature[ord(letter)-ord(ALPHABET[0])] += 1
    # tuples are hashable in contrast to lists
    signature = tuple(signature)
    print(signature)
    signatures[signature] = signatures.get(signature, 0) + 1


res = 0
for count in signatures.values():
  res += count*(count-1)/2

print(int(res))