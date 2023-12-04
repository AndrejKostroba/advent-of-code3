## Advent of Code 2023 - Day 4 - Scratchcards

import pathlib
import re

file = pathlib.Path(__file__).parent.resolve().joinpath('input.txt')

def get_card_numbers(line):
    card = dict()

    [number, numbers] = line.split(':')
    card['card'] = int(re.findall('(\d+)', number)[0])
    card['copies'] = 1

    [winning, picked] = numbers.split('|')
    w = []
    for n in re.findall('(\d+)\s+', winning):
        w.append(int(n))

    card['winning'] = w

    p = []
    for n in re.findall('(\d+)\s+', picked):
        p.append(int(n))
    card['picked'] = p

    # { 'card': n, 'copies': 1, 'winning': [1, 2, 3, 4...], 'picked': [4, 5, 6...] }
    return card

def matching(card):
    winning = card.get('winning')
    picked = card.get('picked')

    matching = []

    for p in picked:
        if p in winning:
            matching.append(p)

    card['matching'] = matching

    # { 'card': n, 'copies': 1, 'winning': [1, 2, 3, 4...], 'picked': [4, 5, 6...], 'matching': [4] }
    return card

def get_points(card):
    if len(card.get('matching')) == 0:
        return 0

    return 2 ** (len(card.get('matching')) - 1)

def resolve_scratchcards(scratchcards):
    for card in scratchcards:
        card_number = card['card']
        copies = card['copies']
        matching = len(card['matching'])

        for i in range(card_number, card_number + matching):
            if i < len(scratchcards):
                scratchcards[i]['copies'] = scratchcards[i]['copies'] + copies

    return scratchcards

with open(file) as f:
    lines = f.readlines()
    part1, part2 = 0, 0

    scratchcards = []
    for line in lines:
        scratchcards.append(matching(get_card_numbers(line)))

    for card in scratchcards:
        part1 += get_points(card)

    for card in resolve_scratchcards(scratchcards):
        part2 += card['copies']

    print('Part 1 :', part1)
    print('Part 2 :', part2)
