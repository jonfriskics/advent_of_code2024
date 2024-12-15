import os
import re

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# ########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<
# """

# input = """
# ##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
# """


def print_matrix(m):
    for l in range(len(m)):
        print(m[l])

map = []
moves = []
rules_split = input.strip().split('\n\n')

for map_lines in rules_split[0].strip().split('\n'):
    for map_line in map_lines.strip().split('\n'):
        l = list()
        for c in map_line:
            l.append(c)
        map.append(l)

for move_lines in rules_split[1].strip().split('\n'):
    for move_line in move_lines.strip().split('\n'):
        for c in move_lines:
            moves.append(c)

robot_position = (0, 0)

for row in range(len(map)):
    for col in range(len(map[0])):
        if map[row][col] == '@':
            robot_position = (row, col)

def gather_boxes(map, row, col, direction_row, direction_col, box_queue):
    # print('in gather', row, col, direction_row, direction_col, box_queue)
    box_queue.append((row, col))
    if map[row + direction_row][col + direction_col] == '.':
        # print('dot found', row, col, box_queue)
        return box_queue
    elif map[row + direction_row][col + direction_col] == '#':
        # print('hash found')
        return []
    elif map[row + direction_row][col + direction_col] == 'O':
        # print('O found')
        # print('in gather O --- ', row, col, direction_row, direction_col, box_queue)
        return gather_boxes(map, row + direction_row, col + direction_col, direction_row, direction_col, box_queue)

for move in moves:
    # print(f'move {move}')

    directions = {'<': (0, -1), '^': (-1, 0), '>': (0, 1), 'v': (1, 0)}

    robot_row = robot_position[0]
    robot_col = robot_position[1]

    row_to_attempt = robot_row + directions[move][0]
    col_to_attempt = robot_col + directions[move][1]

    # print(f'attempt {row_to_attempt}, {col_to_attempt}')
    
    if map[row_to_attempt][col_to_attempt] == '#':
        pass
    elif map[row_to_attempt][col_to_attempt] == 'O':
        boxes_to_move = gather_boxes(map, row_to_attempt, col_to_attempt, directions[move][0], directions[move][1], [])
        # print('boxes to move', boxes_to_move)

        if len(boxes_to_move) > 0:
            while boxes_to_move:
                box_to_move = boxes_to_move[-1]
                # print(f'moving {box_to_move}')
                map[box_to_move[0] + directions[move][0]][box_to_move[1] + directions[move][1]] = 'O'
                map[box_to_move[0]][box_to_move[1]] = '.'
                boxes_to_move.pop()
            map[row_to_attempt][col_to_attempt] = '@'
            map[robot_row][robot_col] = '.'
            robot_position = (row_to_attempt, col_to_attempt)

    elif map[row_to_attempt][col_to_attempt] == '.':
        map[row_to_attempt][col_to_attempt] = '@'
        map[robot_row][robot_col] = '.'
        robot_position = (row_to_attempt, col_to_attempt)
    # print('after')
    # print_matrix(map)

for row in range(len(map)):
    for col in range(len(map[0])):
        if map[row][col] == 'O':
            star1 += (100 * row) + col

print(f'star1: {star1}')
print(f'star2: {star2}')