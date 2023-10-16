
s1 = "hello"
s2 = "wXrXd"

def twoStrings(s1, s2):
  h = {}
  result = "No"
  for i in range(0, max(len(s1), len(s2))):
    if i < len(s1):
      l1 = s1[i]
      if h.get(l1, None) == None: 
        h[l1] = 1
      elif h[l1] < 0:
        result = "Yes"
        break
    if i < len(s2):
      l2 = s2[i]
      if h.get(l2, None) == None:
        h[l2] = -1
      elif h[l2] > 0:
        result = "Yes"
        break
  print(result)