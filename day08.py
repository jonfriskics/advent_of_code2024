import os
import re

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# ..........
# ..........
# ..........
# ....a.....
# ..........
# .....a....
# ..........
# ..........
# ..........
# ..........
# """

# input = """
# ..........
# ..........
# ..........
# ....a.....
# ........a.
# .....a....
# ..........
# ......A...
# ..........
# ..........
# """

# input = """
# ............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............
# """

# input = """
# T.........
# ...T......
# .T........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
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

all_antennas = []

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] != '.':
            all_antennas.append(matrix[row][col])

more_than_one_antenna = set()

for antenna in all_antennas:
    if all_antennas.count(antenna) > 1:
        more_than_one_antenna.add(antenna)

antinodes = set()

for antenna in more_than_one_antenna:
    positions_of_this_antenna = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == antenna:
                positions_of_this_antenna.append((row, col))

    for antenna_position in positions_of_this_antenna:

        antenna_row = antenna_position[0]
        antenna_col = antenna_position[1]

        for antenna_to_diff in positions_of_this_antenna:
            other_antenna_row = antenna_to_diff[0]
            other_antenna_col = antenna_to_diff[1]
            if other_antenna_row != antenna_row and other_antenna_col != antenna_col:
                row_diff = abs(antenna_row - other_antenna_row)
                col_diff = abs(antenna_col - other_antenna_col)

                if antenna_row < other_antenna_row and antenna_col < other_antenna_col:
                    pass
                    # antenna_row is top left of other_antenna
                    antinode1 = (antenna_row - row_diff, antenna_col - col_diff)
                    antinode2 = (antenna_row + row_diff * 2, antenna_col + col_diff * 2)
                    antinodes.add(antinode1)
                    antinodes.add(antinode2)
                elif antenna_row < other_antenna_row and antenna_col > other_antenna_col:
                    # antenna_row is top right of other antenna
                    antinode1 = (antenna_row - row_diff, antenna_col + col_diff)
                    antinode2 = (antenna_row + row_diff * 2, antenna_col - col_diff * 2)
                    antinodes.add(antinode1)
                    antinodes.add(antinode2)
                elif antenna_row > other_antenna_row and antenna_col < other_antenna_col:
                    # antenna_row is bottom left of other antenna
                    antinode1 = (antenna_row + row_diff, antenna_col - col_diff)
                    antinode2 = (antenna_row - row_diff * 2, antenna_col + col_diff * 2)
                    antinodes.add(antinode1)
                    antinodes.add(antinode2)
                elif antenna_row > other_antenna_row and antenna_col > other_antenna_col:
                    # antenna row is bottom right of other antenna
                    antinode1 = (antenna_row + row_diff, antenna_col + col_diff)
                    antinode2 = (antenna_row - row_diff * 2, antenna_col - col_diff * 2)
                    antinodes.add(antinode1)
                    antinodes.add(antinode2)

for antinode in antinodes:
    min_row = 0
    min_col = 0
    max_row = len(matrix)
    max_col = len(matrix[0])

    if (0 <= antinode[0] < len(matrix) and 0 <= antinode[1] < len(matrix[0])):
        star1 += 1



antinodes = set()
total_antennas = 0
positions_of_this_antenna = []
positions_of_any_antenna = []

for antenna in more_than_one_antenna:
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == antenna:
                positions_of_this_antenna.append((row, col))
                positions_of_any_antenna.append((row, col))
                total_antennas += 1

    for antenna_position in positions_of_this_antenna:

        antenna_row = antenna_position[0]
        antenna_col = antenna_position[1]

        for antenna_to_diff in positions_of_this_antenna:
            other_antenna_row = antenna_to_diff[0]
            other_antenna_col = antenna_to_diff[1]
            if other_antenna_row != antenna_row and other_antenna_col != antenna_col:
                row_diff = abs(antenna_row - other_antenna_row)
                col_diff = abs(antenna_col - other_antenna_col)

                if antenna_row < other_antenna_row and antenna_col < other_antenna_col:
                    iterations = 2
                    while iterations < 50:
                        another_antinode1 = (antenna_row - row_diff * (iterations - 1), antenna_col - col_diff * (iterations -1))
                        another_antinode2 = (antenna_row + row_diff * iterations, antenna_col + col_diff * iterations)
                        iterations += 1
                        antinodes.add(another_antinode1)
                        antinodes.add(another_antinode2)

                elif antenna_row < other_antenna_row and antenna_col > other_antenna_col:
                    iterations = 2
                    while iterations < 50:
                        another_antinode1 = (antenna_row - row_diff * (iterations - 1), antenna_col + col_diff * (iterations - 1))
                        another_antinode2 = (antenna_row + row_diff * iterations, antenna_col - col_diff * iterations)
                        iterations += 1
                        antinodes.add(another_antinode1)
                        antinodes.add(another_antinode2)

                elif antenna_row > other_antenna_row and antenna_col < other_antenna_col:
                    iterations = 2
                    while iterations < 50:
                        another_antinode1 = (antenna_row + row_diff * (iterations - 1), antenna_col - col_diff * (iterations - 1))
                        another_antinode2 = (antenna_row - row_diff * iterations, antenna_col + col_diff * iterations)
                        iterations += 1
                        antinodes.add(another_antinode1)
                        antinodes.add(another_antinode2)

                elif antenna_row > other_antenna_row and antenna_col > other_antenna_col:
                    iterations = 2
                    while iterations < 50:
                        another_antinode1 = (antenna_row + row_diff * (iterations - 1), antenna_col + col_diff * (iterations - 1))
                        another_antinode2 = (antenna_row - row_diff * iterations, antenna_col - col_diff * iterations)
                        iterations += 1
                        antinodes.add(another_antinode1)
                        antinodes.add(another_antinode2)
    positions_of_this_antenna = []

for antinode in antinodes:
    min_row = 0
    min_col = 0
    max_row = len(matrix)
    max_col = len(matrix[0])

    if (0 <= antinode[0] < len(matrix) and 0 <= antinode[1] < len(matrix[0])):
        if (antinode[0], antinode[1]) in positions_of_any_antenna:
            pass
        else:
            star2 += 1

star2 += total_antennas

print(f'star1: {star1}')
print(f'star2: {star2}')