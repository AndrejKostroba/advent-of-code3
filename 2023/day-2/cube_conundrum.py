## Advent of Code 2023 - Day 2 - Cube Conundrum

import pathlib
import re

file = pathlib.Path(__file__).parent.resolve().joinpath('input.txt')

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

def get_sets(game):
    splits = game.split(':')[1].split(';')

    sets = []

    for split in splits:
        set = dict()

        for m in re.findall('(\d+) (blue|green|red)', split):
            set[m[1]] = int(m[0])

        sets.append(set)

    return sets

def get_game(game):
    game_num = int(re.findall('Game (\d*)', game)[0])
    sets = get_sets(game)

    return [ game_num, sets ]

def is_valid_game(game):
    for set in game[1]:
        if ('green' in set and set['green'] > GREEN_CUBES) or ('red' in set and set['red'] > RED_CUBES) or ('blue' in set and set['blue'] > BLUE_CUBES):
            return False

    return True

def get_game_score(game):
    if is_valid_game(game):
        return game[0]

    return 0

def get_minimum_needs(game):
    needs = game[1][0]

    for set in game[1][1:]:
        for color in ['green', 'red', 'blue']:
            if (color not in needs and color in set) or (color in set and set[color] > needs[color]):
                needs[color] = set[color]

    return needs

def get_set_power(game):
    needs = get_minimum_needs(game)
    power = 1

    for color in ['green', 'red', 'blue']:
        if color in needs:
            power *= needs[color]

    return power

with open(file) as f:
    lines = f.readlines()
    part1, part2 = 0, 0

    for l in lines:
        part1 += get_game_score(get_game(l))
        part2 += get_set_power(get_game(l))

    print('Part 1 :', part1)
    print('Part 2 :', part2)
