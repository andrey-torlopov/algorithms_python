# Professor Chambouliard hast just discovered a new type of magnet material. He put particles of this material in a box made of small boxes arranged in K rows and N columns as a kind of 2D matrix K x N where K and N are postive integers. He thinks that his calculations show that the force exerted by the particle in the small box (k, n) is:

# v(k, n) = 1 / k *(n + 1)**(2*k)

# Task:

# To help Professor Chambouliard can we calculate the function doubles that will take as parameter maxk and maxn such that doubles(maxk, maxn) = S(maxk, maxn)? Experiences seems to show that this could be something around 0.7 when maxk and maxn are big enough.

# Сложное решение! Не проходит по времени


def doubles(maxk, maxn):
    result = 0
    for k in range(1, maxk+1):
        for n in range(1, maxn+1):
            # dont calculate very small numbers
            if k > 10 and n > 100:
                print("break!")
                break
            result += 1 / (k * (n + 1) ** (2*k))
    return result
