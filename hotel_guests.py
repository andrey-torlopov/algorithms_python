# массив содержит время прихода и ухода гостей
# необходимо найти максимальное количество гостей в отеле

# Пример:
# Входные данные:

from datetime import datetime

arr = [("08:00", "10:30"),
       ("09:15", "11:00"),
       ("10:00", "12:00"),
       ("14:00", "16:30"),
       ("15:00", "17:00")]

# Выходные данные:
# В отеле максимум 3 гостя, в промежуток с 10:00 до 11:00

parsed_arr = [(datetime.strptime(start, "%H:%M").time(), datetime.strptime(end, "%H:%M").time()) for start, end in arr]
# print(parsed_arr)


def max_simultaneous_guests_info(arr):
    # Преобразовать строки в объекты datetime
    intervals = [(datetime.strptime(start, "%H:%M"), datetime.strptime(end, "%H:%M")) for start, end in arr]

    # Создать список событий (приход или уход)
    events = [(start, 1) for start, _ in intervals] + [(end, -1) for _, end in intervals]
    events.sort(key=lambda x: x[0])  # Отсортировать события по времени

    max_guests = 0
    current_guests = 0
    current_start_time = None
    max_interval_start = None
    max_interval_end = None

    for time, change in events:
        if change == 1:
            if current_guests == max_guests:
                current_start_time = time
            current_guests += 1
        else:
            if current_guests == max_guests:
                if max_interval_start is None or (time - current_start_time).seconds > (max_interval_end - max_interval_start).seconds:
                    max_interval_start = current_start_time
                    max_interval_end = time
            current_guests -= 1

        if current_guests > max_guests:
            max_guests = current_guests
            current_start_time = time

    return max_guests, max_interval_start.strftime("%H:%M"), max_interval_end.strftime("%H:%M")


arr = [("08:00", "10:30"),
       ("09:15", "11:00"),
       ("10:00", "12:00"),
       ("14:00", "16:30"),
       ("15:00", "17:00")]

max_guests, start_time, end_time = max_simultaneous_guests_info(arr)
print(f"Максимальное количество гостей: {max_guests}")
print(f"Они находились в отеле с {start_time} до {end_time}")
