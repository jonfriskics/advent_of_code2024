import os
import re

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

matrix = []
guard_start = ()
for i in input.strip().split("\n"):
    l = list()
    for s in i:
        l.append(s)
    matrix.append(l)

def pad_matrix_with_x(matrix):
    max_cols = len(matrix[0])
    padded_row = ['x'] * (max_cols + 2)
    padded_matrix = [padded_row] + [['x'] + row + ['x'] for row in matrix] + [padded_row]
    return padded_matrix

matrix = pad_matrix_with_x(matrix)

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == '^':
            guard_start = (row, col)

direction = [(-1,0),(0,1),(1,0),(0,-1)]
current_direction = 0

current_row = guard_start[0]
current_col = guard_start[1]
next_step_row = guard_start[0] + direction[current_direction][0]
next_step_col = guard_start[1] + direction[current_direction][1]

visited_steps = []

while(matrix[next_step_row][next_step_col] != 'x'):
    if matrix[next_step_row][next_step_col] == '.' or matrix[next_step_row][next_step_col] == '^':
        current_row = next_step_row
        current_col = next_step_col
        next_step_row = current_row + direction[current_direction][0]
        next_step_col = current_col + direction[current_direction][1]
        current_direction = current_direction
        visited_steps.append((current_row, current_col))
    elif matrix[next_step_row][next_step_col] == '#':
        current_direction += 1
        if current_direction == 4:
            current_direction = 0
        next_step_row = current_row + direction[current_direction][0]
        next_step_col = current_col + direction[current_direction][1]

visited_set = {v for v in visited_steps}
star1 = len(visited_set)

def try_matrix(matrix):
    direction = [(-1,0),(0,1),(1,0),(0,-1)]
    current_direction = 0

    current_row = guard_start[0]
    current_col = guard_start[1]
    next_step_row = guard_start[0] + direction[current_direction][0]
    next_step_col = guard_start[1] + direction[current_direction][1]

    loop_count = 0
    while(matrix[next_step_row][next_step_col] != 'x' and loop_count < 10000):
        if matrix[next_step_row][next_step_col] == '.' or matrix[next_step_row][next_step_col] == '^':
            current_row = next_step_row
            current_col = next_step_col
            next_step_row = current_row + direction[current_direction][0]
            next_step_col = current_col + direction[current_direction][1]
            current_direction = current_direction
            visited_steps.append((current_row, current_col))
        elif matrix[next_step_row][next_step_col] == '#':
            current_direction += 1
            if current_direction == 4:
                current_direction = 0
            next_step_row = current_row + direction[current_direction][0]
            next_step_col = current_col + direction[current_direction][1]
        loop_count += 1
    return loop_count

for row in range(1,len(matrix)-1):
    for col in range(1,len(matrix[row])-1):
        original_value = matrix[row][col]
        if matrix[row][col] == '.':
            matrix[row][col] = '#'
        loop_count = try_matrix(matrix)
        if loop_count == 10000:
            star2 += 1
        matrix[row][col] = original_value

print(f'star1: {star1}')
print(f'star2: {star2}')