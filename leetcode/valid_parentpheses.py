def isValid(s: str) -> bool:
    stack = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if (i == ')' and last != '(') or (i == '}' and last != '{') or (i == ']' and last != '['):
                return False
    return len(stack) == 0


print(isValid("()"))
