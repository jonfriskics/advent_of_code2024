import os
import re
import math

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

# input = """
# AAAA
# BBCD
# BBCC
# EEEC
# """

# input = """
# OOOOO
# OXOXO
# OOOOO
# OXOXO
# OOOOO
# """

# input = """
# RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE
# """

star1 = 0
star2 = 0

def print_matrix(m):
    for l in range(len(m)):
        print(m[l])

matrix = []
for i in input.strip().split("\n"):
    l = list()
    for s in i:
        l.append(s)
    matrix.append(l)

letters = set()

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        letters.add(matrix[row][col])

def calculate_island_areas_and_perimeters(matrix):
    max_rows = len(matrix)
    max_cols = len(matrix[0])
    visited = [[False] * max_cols for _ in range(max_rows)]
    islands = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # had to seek a lot of help on this one!
    def flood_fill(r, c, letter):
        stack = [(r, c)]
        visited[r][c] = True
        area = 0
        perimeter = 0

        while stack:
            x, y = stack.pop()
            area += 1

            for direction_x, direction_y in directions:
                neighbor_x, neighbor_y = x + direction_x, y + direction_y
                if 0 <= neighbor_x < max_rows and 0 <= neighbor_y < max_cols:
                    if matrix[neighbor_x][neighbor_y] == letter:
                        if not visited[neighbor_x][neighbor_y]:
                            visited[neighbor_x][neighbor_y] = True
                            stack.append((neighbor_x, neighbor_y))
                    elif matrix[neighbor_x][neighbor_y] != letter:
                        perimeter += 1
                else:
                    perimeter += 1

        return area, perimeter

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if not visited[row][col]:
                letter = matrix[row][col]
                area, perimeter = flood_fill(row, col, letter)
                islands.append({
                    "letter": letter,
                    "area": area,
                    "perimeter": perimeter,
                })

    return islands

islands = calculate_island_areas_and_perimeters(matrix)

for island in islands:
    star1 += island['area'] * island['perimeter']
    print(island)

print(f'star1: {star1}')
print(f'star2: {star2}')