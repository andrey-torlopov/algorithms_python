# Дан упорядоченный строго по возрастанию массив и число n.
# Нужно найти 2 числа в массиве, которые в сумме дают n.

import random

# Создаем пустой список для хранения чисел
random_numbers = []

# Начальное число
current_number = random.randint(1, 10)  # Генерируем начальное число случайным образом

# Генерируем последовательность из 50 чисел
for _ in range(20):
    random_numbers.append(current_number)
    current_number += random.randint(1, 10)  # Увеличиваем число на случайное значение от 1 до 10

print(random_numbers)
