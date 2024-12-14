import os
import re
from itertools import permutations

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

# input = """
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279
# """

star1 = 0
star2 = 0

combinations = []
for a in range(1,101):
    for b in range(1,101):
        combinations.append({'A': a, 'B': b})

print('combinations built')

for behaviors in input.strip().split('\n\n'):
    matches = re.search(r'Button\sA\:\sX\+(\d+),\sY\+(\d+)\s+Button\sB\:\sX\+(\d+),\sY\+(\d+)\s+Prize\:\sX\=(\d+),\sY\=(\d+)', behaviors)

    a_x = matches[1]
    a_y = matches[2]
    b_x = matches[3]
    b_y = matches[4]
    p_x = matches[5]
    p_y = matches[6]

    # print(a_x, a_y, b_x, b_y, p_x, p_y)

    # print(combinations)
    total_tokens_spent = 0
    positions_matched = []
    for combination in combinations:
        a_presses = combination['A']
        b_presses = combination['B']

        current_position = (0, 0)

        # print(f'combination {combination}')

        tokens_spent = 100000000000

        for a_press in range(1,a_presses+1):
            new_x = current_position[0] + int(a_x)
            new_y = current_position[1] + int(a_y)
            current_position = (new_x, new_y)
        for b_press in range(1, b_presses+1):
            new_x = current_position[0] + int(b_x)
            new_y = current_position[1] + int(b_y)
            current_position = (new_x, new_y)
        if current_position[0] == int(p_x) and current_position[1] == int(p_y):
            positions_matched.append((a_press, b_press))
    min_tokens = 100000000
    for positions in positions_matched:
        tokens_spent = positions[0] * 3 + positions[1] * 1
        if tokens_spent < min_tokens:
            min_tokens = tokens_spent
    if min_tokens == 100000000:
        min_tokens = 0
    star1 += min_tokens
    # print(f'min tokens {min_tokens}')

print(f'star1: {star1}')
print(f'star2: {star2}')