## Advent of Code 2023 - Day 3 - Gear Ratios

import pathlib
import re

file = pathlib.Path(__file__).parent.resolve().joinpath('input.txt')

def get_numbers_with_coordonnates(lines):
    numbers = []

    for index, line in enumerate(lines):
        for find in re.finditer('(\d+)', line):
            numbers.append([[index, find.span()[0]], [index, find.span()[1] - 1], int(find.group())])

    return numbers

def get_testing_area(number, sizes):
    area = []

    # prevent OOB vertically
    if number[0][0] > 0:
        for x in range(number[0][1] - 1, number[1][1] + 2):
            # prevent OOB horizontally
            if x >= 0 and x < sizes[1] - 1:
                area.append([ number[0][0] - 1, x ])

    # prevent OOB vertically
    if number[0][1] > 0:
        area.append([ number[0][0], number[0][1] - 1 ])

    # prevent OOB vertically
    if number[1][1] < sizes[0] - 1:
        area.append([ number[1][0], number[1][1] + 1 ])

    # prevent OOB vertically
    if number[0][0] < sizes[0] - 1:
        for x in range(number[0][1] - 1, number[1][1] + 2):
            # prevent OOB horizontally
            if x >= 0 and x < sizes[1] - 1:
                area.append([ number[0][0] + 1, x ])

    return area

def is_symbol(char):
    return True if re.match('[^\d\s\w.]', char) else False

def test_neighbors(number, lines):
    area = get_testing_area(number, [ len(lines), len(lines[0]) ])

    for coordonnates in area:
        if is_symbol(lines[coordonnates[0]][coordonnates[1]]):
            return True

    return False

def get_number_area(number, lines):
    return [get_testing_area(number, [ len(lines), len(lines[0]) ]), number[2]]

def is_gear(a, b, lines):
    for ca in a[0]:
        for cb in b[0]:
            if ca[0] == cb[0] and ca[1] == cb[1] and lines[ca[0]][ca[1]] == '*':
                return True

    return False

def get_gears_ratios(numbers, lines):
    areas = []
    gears_ratios = []

    for num in numbers:
        areas.append(get_number_area(num, lines))

    for index, a in enumerate(areas):
        for b in areas[index + 1:]: # ignore current a area to prevent duplicated ratio
            if is_gear(a, b, lines):
                gears_ratios.append([a[1], b[1]])

    return gears_ratios

with open(file) as f:
    lines = f.readlines()
    part1, part2 = 0, 0

    numbers = get_numbers_with_coordonnates(lines)
    for num in numbers:
        part1 += num[2] if test_neighbors(num, lines) else 0
    print('Part 1 :', part1)

    ratios = get_gears_ratios(numbers, lines)
    for ratio in ratios:
        part2 += (ratio[0] * ratio[1])

    print('Part 2 :', part2)
