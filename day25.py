import os
import re

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# #####
# .####
# .####
# .####
# .#.#.
# .#...
# .....

# #####
# ##.##
# .#.##
# ...##
# ...#.
# ...#.
# .....

# .....
# #....
# #....
# #...#
# #.#.#
# #.###
# #####

# .....
# .....
# #.#..
# ###..
# ###.#
# ###.#
# #####

# .....
# .....
# .....
# #....
# #.#..
# #.#.#
# #####
# """

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

def make_heights(schematic):
    pattern = []
    for i in schematic.strip().split("\n"):
        l = list()
        for s in i:
            l.append(s)
        pattern.append(l)

    rotated = list(zip(*pattern))[::-1]

    converted = []
    for row in range(len(rotated)):
        hash_count = 0
        for col in range(1,len(rotated[0])-1):
            if rotated[row][col] == '#':
                hash_count += 1
        converted.append(hash_count)
    return converted[::-1]

schematics = input.strip().split('\n\n')

locks = []
keys = []

max_rows = 7
max_cols = 5

for schematic in schematics:
    if schematic[0][0] == '#':
        locks.append(make_heights(schematic))
    elif schematic[0][0] == '.':
        keys.append(make_heights(schematic))

for lock in locks:
    for key in keys:
        if lock[0] + key[0] <= 5 and lock[1] + key[1] <= 5 and lock[2] + key[2] <= 5 and lock[3] + key[3] <= 5 and lock[4] + key[4] <= 5:
            star1 += 1

print(f'star1: {star1}')
print(f'star2: {star2}')