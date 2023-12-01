## Advent of Code 2023 - Day 0 - Model

import pathlib

file = pathlib.Path(__file__).parent.resolve().joinpath('input.txt')

with open(file) as f:
    lines = f.readlines()
    part1, part2 = '', ''

    print('part 1', part1)
    print('part 2', part2)
