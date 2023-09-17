# задача со скобками

class BracketStack:
    items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def is_braces_seq_correct(string: str) -> bool:
    """
    Проверяет корректность скобочной последовательности
    >>> is_braces_seq_correct("()[]")
    True
    >>> is_braces_seq_correct("([)]")
    False
    """
    stack = BracketStack()

    for item in string:
        if item not in ('[', ']', '(', ')'):
            continue
        # if item == '(' or item == '[':
        if item in '([':
            stack.push(item)
        elif item == ')' or item == ']':
            if stack.is_empty():
                return False
            else:
                left = stack.pop()
                if not ((left == '(' and item == ')') or (left == '[' and item == ']')):
                    return False

    return stack.is_empty()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
