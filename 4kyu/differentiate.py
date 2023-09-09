# Differentiate a polynomial
# Create a function that differentiates a polynomial for a given value of x.

# Your function will receive 2 arguments: a polynomial as a string, and a point to evaluate the equation as an integer.

# Assumptions:

# There will be a coefficient near each x, unless the coefficient equals 1 or -1.
# There will be an exponent near each x, unless the exponent equals 0 or 1.
# All exponents will be greater or equal to zero

# differenatiate("12x+2", 3)      ==>   returns 12
# differenatiate("x^2+3x+2", 3)   ==>   returns 9

def process_term(term) -> (int, int):
    if 'x^' in term:
        coeff_part, power_part = term.split('x^')
        coeff_part = '1' if coeff_part == '' else coeff_part
        coeff_part = '-1' if coeff_part == '-' else coeff_part
        return int(coeff_part), int(power_part)
    elif 'x' in term:
        coeff_part = term.replace('x', '')
        coeff_part = '1' if coeff_part == '' else coeff_part
        coeff_part = '-1' if coeff_part == '-' else coeff_part
        return int(coeff_part), 1
    else:
        return int(term), 0


def differentiate(equation, point):
    equation = equation.replace(" ", "")
    equation = equation.replace('-', '+-')
    terms = equation.split("+")
    if terms[0] == '':
        terms = terms[1:]

    coefficients = []
    powers = []

    for item in terms:
        subcoef, subpow = process_term(item)
        coefficients.append(subcoef)
        powers.append(subpow)

    terms = list(zip(coefficients, powers))
    terms = list(map(lambda x: (x[0] * x[1], x[1] - 1), terms))
    terms = list(filter(lambda x: x[1] >= 0, terms))
    result = 0
    for coefficient, power in terms:
        result += coefficient * (point ** power)

    return result


def differentiate2(equation, point):
    terms = list(filter(lambda x: 'x' in x, equation.replace('-', '+-').split("+")))
    sum = 0
    for i in terms:
        split_i = i.split('x')
        split_i[0] = split_i[0] + '1' if split_i[0] == '' or split_i[0] == '-' else split_i[0]
        split_i[1] = '^1' if split_i[1] == '' else split_i[1]
        sum += int(split_i[0]) * int(split_i[1][1:]) * (point**(int(split_i[1][1:])-1))
    return sum


# Пример использования
e = "-x^2+3x-3"
print(e, differentiate(e, 3))
