import os
import re
import heapq

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# ###############
# #.......#....E#
# #.#.###.#.###.#
# #.....#.#...#.#
# #.###.#####.#.#
# #.#.#.......#.#
# #.#.#####.###.#
# #...........#.#
# ###.#.#####.#.#
# #...#.....#.#.#
# #.#.#.###.#.#.#
# #.....#...#.#.#
# #.###.#.#.#.#.#
# #S..#.....#...#
# ###############
# """

# input = """
# #################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################
# """

def print_matrix(m):
    for l in range(len(m)):
        print(m[l])

matrix = []
start = (0, 0)
end = (0, 0)
for i in input.strip().split("\n"):
    l = list()
    for s in i:
        l.append(s)
    matrix.append(l)

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 'S':
            start = (row, col)
        if matrix[row][col] == 'E':
            end = (row, col)

def which_direction(start_row, start_col, end_row, end_col):
    if end_row - start_row == -1 and end_col - start_col == 0:
        return 'up'
    elif end_row - start_row == 1 and end_col - start_col == 0:
        return 'down'
    elif end_row - start_row == 0 and end_col - start_col == 1:
        return 'right'
    elif end_row - start_row == 0 and end_col - start_col == -1:
        return 'left'

def calculate_path_score(path):
    score = 0
    turns = 0
    current_direction = 'right'
    for i, coord in enumerate(path):

        if i == 0:
            current_direction = 'right'
        else:
            current_row = path[i][0]
            current_col = path[i][1]
            last_row = path[i-1][0]
            last_col = path[i-1][1]
            direction_moved = which_direction(last_row, last_col, current_row, current_col)

            if current_direction != direction_moved:
                turns += 1
            current_direction = direction_moved
    return (turns * 1000 + len(path) - 1)

# got some help on this one!
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

            if 0 <= neighbor_row < max_rows and 0 <= neighbor_col < max_cols and matrix[neighbor_row][neighbor_col] != "#":
                turn_penalty = 0
                if current_direction != next_direction:
                    turn_penalty = 1000

                heapq.heappush(heap, (cost + 1 + turn_penalty, neighbor_row, neighbor_col, next_direction, path_length + 1))
    return -1

star1 = a_star(matrix, start, end)

print(f'star1: {star1}')
print(f'star2: {star2}')