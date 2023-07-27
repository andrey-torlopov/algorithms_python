# ROT13 is a simple letter substitution cipher that replaces a letter with the
# letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string, they should be
# returned as they are. Only letters from the latin/english alphabet should be shifted,
# like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

# def next_letter(letter):
#     # Получаем кодовое значение текущей буквы
#     # Проверяем, является ли буква строчной или заглавной

#     # Увеличиваем кодовое значение на 1
#     next_code = ord(letter) + 13
#     diff = next_code - ord('Z') if letter.isupper() else next_code - ord('z')
#     next_code = ord('A') + diff if letter.isupper() and diff > 0 else ord('a') + diff

#     # Преобразуем кодовое значение обратно в символ и возвращаем его
#     return chr(next_code)


# Примеры использования
# print(next_letter('a'))  # Вывод: 'b'
# print(next_letter('x'))  # Вывод: 'y'
# print(next_letter('Z'))  # Вывод: 'A'
# print(next_letter('z'))  # Вывод: 'a'


from curses.ascii import isalpha


def rot13(message: str) -> str:
    result = []
    for letter in message:
        if not letter.isalpha():
            result.append(letter)
        else:
            base = ord('A') if letter.isupper() else ord('a')
            next_code = (ord(letter) - base + 13) % 26 + base
            result.append(chr(next_code))
    return "".join(result)


print(rot13('test'))  # grfg
