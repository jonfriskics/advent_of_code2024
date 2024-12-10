import os
import re

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# 12345
# """

# input = """
# 2333133121414131402
# """

# input = """
# 1313165
# """

# input = """
# 233313312141413140233
# """

total_dots = 0
for line in input.strip().split('\n'):
    numbers = [c for c in line]
    id = 0
    blocks = []
    for i, n in enumerate(numbers):
        if i % 2 == 0:
            for i in range(int(n)):
                blocks.append(str(id))
        else:
            if int(n) > 0:
                for i in range(int(n)):
                    blocks.append(str('.'))
                total_dots += 1 * int(n)
            id += 1

    og_blocks = blocks.copy()

    trip = 0
    while(blocks.index('.') < len(blocks)-total_dots):
        dot_index = blocks.index('.')
        for i, c in enumerate(reversed(blocks)):
            if c != '.':
                result_index = len(blocks) - 1 - i
                blocks[dot_index] = blocks[result_index]
                blocks[result_index] = '.'
                break
    for i, n in enumerate(blocks):
        if n == '.':
            break
        star1 += int(n) * i

def find_first_group(og_blocks, c):
    c = str(c)
    start_index = None
    positions = []
    
    for i, char in enumerate(og_blocks):
        if char == c:
            if start_index is None:
                start_index = i
            positions.append(i)
        else:
            if start_index is not None:
                break

    return positions if start_index is not None else []

def find_dot_group_by_length(og_blocks, length):
    current_group = []
    
    for i, char in enumerate(og_blocks):
        if char == '.':
            current_group.append(i)
            if len(current_group) == length:
                return current_group
        else:
            current_group = []
    
    return []

next_highest_number = int(max(og_blocks))

while next_highest_number > 0:
    next_highest_number_positions = find_first_group(og_blocks, next_highest_number)
    dot_set_positions = find_dot_group_by_length(og_blocks, len(next_highest_number_positions))

    dot_position = 0
    runs = 0
    if len(dot_set_positions) > 0 and max(dot_set_positions) < min(next_highest_number_positions):
        for num_position in next_highest_number_positions:
            dot_pos = dot_set_positions[dot_position]
            og_blocks[dot_pos] = str(next_highest_number)
            og_blocks[num_position] = str('.')
            dot_position += 1
            runs += 1
    
    next_highest_number -= 1

for a, n in enumerate(og_blocks):
    if n == '.':
        continue
    star2 += int(n) * a

print(f'star1: {star1}')
print(f'star2: {star2}')