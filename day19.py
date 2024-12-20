import os
import re
from functools import cache

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# r, wr, b, g, bwu, rb, gb, br

# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb
# """

towel_patterns = []
designs = []

rules = input.strip().split('\n\n')

for rule in rules[0].strip().split(', '):
    towel_patterns.append(rule)

for rule in rules[1].strip().split('\n'):
    designs.append(rule)

@cache
def find_pattern(design, towel_patterns):
    if len(design) == 0:
        return 1

    sub_sequence = 0
    for idx in range(len(design)):
        towel = design[0:idx+1]
        if towel in towel_patterns:
            sub_sequence += find_pattern(design[idx+1:], towel_patterns)
            if sub_sequence == 1:
                return 1

    return sub_sequence

@cache
def find_all_patterns(design, towel_patterns):
    if len(design) == 0:
        return 1

    total = 0
    for idx in range(len(design)):
        towel = design[0:idx+1]
        if towel in towel_patterns:
            total += find_all_patterns(design[idx+1:], towel_patterns)

    return total

for design in designs:
    if find_pattern(design, tuple(towel_patterns)):
        star1 += 1
    star2 += find_all_patterns(design, tuple(towel_patterns))

print(f'star1: {star1}')
print(f'star2: {star2}')