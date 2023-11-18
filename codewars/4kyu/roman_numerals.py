# Перевод чисел в римские и обратно
class RomanNumerals:
    @staticmethod
    def to_roman(decimal_num: int) -> str:
        if not 1 <= decimal_num <= 3999:
            raise ValueError("Число должно быть в диапазоне от 1 до 3999.")

        roman_mapping = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        roman_numeral = ''
        for value, symbol in roman_mapping.items():
            while decimal_num >= value:
                roman_numeral += symbol
                decimal_num -= value

        return roman_numeral

    @staticmethod
    def from_roman(roman_num: str) -> int:
        roman_values = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        result = 0
        i = 0
        while i < len(roman_num):
            if i + 1 < len(roman_num) and roman_values[roman_num[i]] < roman_values[roman_num[i + 1]]:
                result += roman_values[roman_num[i + 1]] - roman_values[roman_num[i]]
                i += 2
            else:
                result += roman_values[roman_num[i]]
                i += 1

        return result


if __name__ == '__main__':
    print(RomanNumerals.from_roman('MCXVI'))
