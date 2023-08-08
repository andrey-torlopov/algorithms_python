# In a grid of 4 by 4 squares you want to place a skyscraper in each square with only
# some clues:

# The height of the skyscrapers is between 1 and 4
# No two skyscrapers in a row or column may have the same number of floors
# A clue is the number of skyscrapers that you can see in a row or column from the outside
# Higher skyscrapers block the view of lower skyscrapers located behind them

# Can you write a program that can solve this puzzle?

# Example:

# To understand how the puzzle works, this is an example of a row with 2 clues. Seen
# from the left side there are 4 buildings visible while seen from the right side only 1:

from itertools import permutations


def visible_number(line):
    return len(set(max(line[:i + 1]) for i in range(len(line))))


def is_valid(grid, clues):
    grid1 = tuple(zip(*grid))
    grid2 = tuple(row[::-1] for row in grid)
    grid3 = tuple(zip(*grid[::-1]))[::-1]
    grid4 = grid[::-1]
    for i, line in enumerate(grid1 + grid2 + grid3 + grid4):
        if i < 4 and set(line) != {1, 2, 3, 4}:
            return False
        if clues[i] and visible_number(line) != clues[i]:
            return False
    return True


def solve_puzzle(clues):
    for grid in permutations(permutations(range(1, 5)), r=4):
        if is_valid(grid, clues):
            return grid
    return
