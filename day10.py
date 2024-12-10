import os
import re

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# 0123
# 1234
# 8765
# 9876
# """

# input = """
# ...0...
# ...1...
# ...2...
# 6543456
# 7.....7
# 8.....8
# 9.....9
# """

# input = """
# ..90..9
# ...1.98
# ...2..7
# 6543456
# 765.987
# 876....
# 987....
# """

# input = """
# 10..9..
# 2...8..
# 3...7..
# 4567654
# ...8..3
# ...9..2
# .....01
# """

# input = """
# 89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732
# """

# input = """
# .....0.
# ..4321.
# ..5..2.
# ..6543.
# ..7..4.
# ..8765.
# ..9....
# """

# input = """
# ..90..9
# ...1.98
# ...2..7
# 6543456
# 765.987
# 876....
# 987....
# """

# input = """
# 012345
# 123456
# 234567
# 345678
# 4.6789
# 56789.
# """

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

matrix = []
for i in input.strip().split("\n"):
    l = list()
    for s in i:
        if s == '.':
            l.append(999)
        else:
            l.append(int(s))
    matrix.append(l)

def get_paths(matrix, start, end):
    max_rows = len(matrix)
    max_cols = len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    all_paths = []

    def dfs(row, col, path):
        if (row, col) == end:
            all_paths.append(path.copy())
            return

        current_value = matrix[row][col]

        for direction_x, direction_y in directions:
            next_row = row + direction_x
            next_col = col + direction_y

            if ((0 <= next_row < max_rows) and (0 <= next_col < max_cols) and (matrix[next_row][next_col] == current_value + 1) and ((next_row, next_col) not in path)):
                path.append((next_row, next_col))
                dfs(next_row, next_col, path)
                path.pop()

    dfs(start[0], start[1], [start])
    return all_paths

nines = []

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 9:
            nines.append((row, col))

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 0:
            for nine in nines:
                paths = get_paths(matrix, (row,col), (nine[0],nine[1]))
                if len(paths) > 0:
                    star1 += 1
                    star2 += len(paths)

print(f'star1: {star1}')
print(f'star2: {star2}')