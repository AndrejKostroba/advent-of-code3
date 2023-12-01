## Advent of Code 2023 - Day 1 - Trebuchet

import pathlib
import re

file = pathlib.Path(__file__).parent.resolve().joinpath('input.txt')

spelled_out = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_digits(str):
    digits = []

    for index, char in enumerate(str):
        if char.isdigit():
            digits.append(int(char))

    return digits

def get_spelled_out_digits(str):
    digits = []

    # ?= for overlap
    for m in re.findall("(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))", str):
        if m.isdigit():
            digits.append(int(m))
        else:
            digits.append(spelled_out.index(m))
    return digits

def two_digits(digits):
    if len(digits) == 0:
        return 0

    return digits[0] * 10 + digits[-1]

with open(file) as f:
    lines = f.readlines()
    part1, part2 = 0, 0
    for l in lines:
        part1 += two_digits(get_digits(l))
        part2 += two_digits(get_spelled_out_digits(l))

    print('Part 1 :', part1)
    print('Part 2 :', part2)
