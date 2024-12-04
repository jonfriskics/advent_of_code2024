import os
import re

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....
# """

# input = """
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """

# input = """
# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........
# """

# input = """
# M.M
# .A.
# S.S
# """

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

matrix = []
for i in input.strip().split("\n"):
    l = list()
    for s in i:
        l.append(s)
    matrix.append(l)

def pad_matrix_with_dots(matrix):
    max_cols = len(matrix[0])
    padded_row = ['.'] * (max_cols + 4)
    padded_matrix = [padded_row, padded_row] + [['.','.'] + row + ['.','.'] for row in matrix] + [padded_row, padded_row]
    return padded_matrix

matrix = pad_matrix_with_dots(matrix)

directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        current_row = row
        current_col = col
        current_direction = ()

        if matrix[row][col] == 'X':
            for direction in directions:
                if matrix[row+direction[0]][col+direction[1]] == 'M':
                    m_row = row + direction[0]
                    m_col = col + direction[1]
                    locked_direction = (direction[0], direction[1])
                    if matrix[m_row+locked_direction[0]][m_col+locked_direction[1]] == 'A':
                        a_row = m_row + locked_direction[0]
                        a_col = m_col + locked_direction[1]
                        if matrix[a_row+locked_direction[0]][a_col+locked_direction[1]] == 'S':
                            star1 += 1

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        current_row = row
        current_col = col
        current_direction = ()

        if (matrix[row][col] == 'M'):
            if (matrix[row+1][col+1] == 'A' and matrix[row+2][col+2] == 'S' and matrix[row][col+2] == 'M' and matrix[row+2][col] == 'S') or (matrix[row+1][col+1] == 'A' and matrix[row+2][col+2] == 'S' and matrix[row][col+2] == 'S' and matrix[row+2][col] == 'M'):
                star2 += 1
        elif (matrix[row][col] == 'S'):
            if (matrix[row+1][col+1] == 'A' and matrix[row+2][col+2] == 'M' and matrix[row][col+2] == 'M' and matrix[row+2][col] == 'S') or (matrix[row+1][col+1] == 'A' and matrix[row+2][col+2] == 'M' and matrix[row][col+2] == 'S' and matrix[row+2][col] == 'M'):
                star2 += 1

print(f'star1: {star1}')
print(f'star2: {star2}')