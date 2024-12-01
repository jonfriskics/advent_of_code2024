import os
import re
import math

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# """

left_numbers = []
right_numbers = []

for line in input.split('\n'):
    left = int(line.split()[0])
    right = int(line.split()[1])
    left_numbers.append(left)
    right_numbers.append(right)

left_numbers.sort()
right_numbers.sort()

for n in range(len(left_numbers)):
    star1 += abs(left_numbers[n] - right_numbers[n])

for n in range(len(left_numbers)):
    found_count = 0
    for a in range(len(right_numbers)):
        if left_numbers[n] == right_numbers[a]:
            found_count += 1
    star2 += (left_numbers[n] * found_count)

print(f'star1: {star1}')
print(f'star2: {star2}')