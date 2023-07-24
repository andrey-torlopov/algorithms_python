def sum_two_smallest_numbers(numbers: list[int]) -> int:
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0] + sorted_numbers[1]


def sum_two_smallest_numbers_2(numbers: list[int]) -> int:
    return sum(sorted(numbers)[:2])
