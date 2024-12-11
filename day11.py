import os
import re
from functools import cache

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# 0 1 10 99 999
# """

# input = """
# 125 17
# """

stones = input.strip().split("\n")[0].split(' ')

blinks = 25

while blinks > 0:
    new_stones = []
    for i, n in enumerate(stones):
        if n == "0":
            new_stones.append("1")
        elif len(n) % 2 == 0:
            midpoint = len(n)//2
            left_side = n[:midpoint]
            right_side = n[midpoint:]
            new_stones.append(str(int(left_side)))
            new_stones.append(str(int(right_side)))
        else:
            new_stones.append(str(int(n) * 2024))
    stones = new_stones.copy()
    blinks -= 1

star1 = len(stones)

print(f'star1: {star1}')
print(f'star2: {star2}')