import os
import re
import heapq

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# 5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0
# """

# max_rows = 6
# max_cols = 6

max_rows = 70
max_cols = 70

def print_matrix(m):
    for l in range(len(m)):
        print(m[l])

matrix = []
for i in range(max_rows+1):
    l = list()
    for j in range(max_cols+1):
        l.append('.')
    matrix.append(l)

counter = 0
for line in input.strip().split('\n'):
    if counter == 1024:
        break
    row = int(line.strip().split(',')[1])
    col = int(line.strip().split(',')[0])

    matrix[row][col] = 'X'
    counter += 1

start = (0,0)
end = (max_rows, max_cols)

def a_star(matrix, start, end):
    max_rows = len(matrix)
    max_cols = len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_names = ['right', 'down', 'left', 'up']
    heap = [(0, start[0], start[1], 'right', 0)]
    visited_points = set()

    while heap:
        cost, row, col, current_direction, path_length = heapq.heappop(heap)

        if (row, col) == end:
            return cost
        
        if (row, col, current_direction) in visited_points:
            continue
        
        visited_points.add((row, col, current_direction))

        for i, (direction_row, direction_col) in enumerate(directions):
            neighbor_row = row + direction_row
            neighbor_col = col + direction_col
            next_direction = direction_names[i]

            if 0 <= neighbor_row < max_rows and 0 <= neighbor_col < max_cols and matrix[neighbor_row][neighbor_col] != "X":
                turn_penalty = 0
                # if current_direction != next_direction:
                #     turn_penalty = 1000

                heapq.heappush(heap, (cost + 1 + turn_penalty, neighbor_row, neighbor_col, next_direction, path_length + 1))
    return -1

star1 = a_star(matrix, start, end)

matrix = []
for i in range(max_rows+1):
    l = list()
    for j in range(max_cols+1):
        l.append('.')
    matrix.append(l)

for line in input.strip().split('\n'):
    row = int(line.strip().split(',')[1])
    col = int(line.strip().split(',')[0])

    matrix[row][col] = 'X'

    if a_star(matrix, start, end) == -1:
        star2 = f'{str(col)},{str(row)}'
        break

print(f'star1: {star1}')
print(f'star2: {star2}')