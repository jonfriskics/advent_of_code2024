import os
import re
import heapq

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

input = """
029A
980A
179A
456A
379A
"""

input = """
179A
"""

def print_matrix(m):
    for l in range(len(m)):
        print(m[l])
    print()

numpad = []
for r in range(4):
    l = list()
    for c in range(3):
        l.append('.')
    numpad.append(l)

numpad[0][0] = '7'
numpad[0][1] = '8'
numpad[0][2] = '9'
numpad[1][0] = '4'
numpad[1][1] = '5'
numpad[1][2] = '6'
numpad[2][0] = '1'
numpad[2][1] = '2'
numpad[2][2] = '3'
numpad[3][0] = 'X'
numpad[3][1] = '0'
numpad[3][2] = 'A'

# print_matrix(numpad)

keypad = []
for r in range(2):
    l = list()
    for c in range(3):
        l.append('.')
    keypad.append(l)

keypad[0][0] = 'X'
keypad[0][1] = '^'
keypad[0][2] = 'A'
keypad[1][0] = '<'
keypad[1][1] = 'v'
keypad[1][2] = '>'

# print_matrix(keypad)

def a_star(matrix, start, end):
    max_rows = len(matrix)
    max_cols = len(matrix[0])
    directions = [(0, -1),(1, 0), (0, 1), (-1, 0)]
    direction_names = ['left', 'down', 'right', 'up']
    heap = [(0, start[0], start[1], 0, [], None)]
    visited_points = set()

    while heap:
        cost, row, col, path_length, path, last_direction = heapq.heappop(heap)

        if (row, col) == end:
            return cost, path
        
        if (row, col) in visited_points:
            continue
        
        visited_points.add((row, col))

        for i, (direction_row, direction_col) in enumerate(directions):
            neighbor_row = row + direction_row
            neighbor_col = col + direction_col
            next_direction = direction_names[i]

            if 0 <= neighbor_row < max_rows and 0 <= neighbor_col < max_cols and matrix[neighbor_row][neighbor_col] != "#" and matrix[neighbor_row][neighbor_col] != 'X':

                direction_penalty = 0 
                if next_direction == last_direction:
                    direction_penalty = 0
                else:
                    direction_penalty = 1

                heapq.heappush(heap, (cost + 1 + direction_penalty, neighbor_row, neighbor_col, path_length + 1, path + [next_direction], next_direction))
    return -1, []

# numeric keypad
start = (3, 2)
steps = []
for code in input.strip().split('\n'):
    code_pieces = list(code)
    for code_piece in code_pieces:
        movement = dict()
        movement['start'] = start
        for row in range(len(numpad)):
            for col in range(len(numpad[0])):
                if numpad[row][col] == code_piece:
                    end = (row, col)
                    movement['end'] = (row, col)
                    start = end
        steps.append(movement)

    numpad_directions = ''
    for step in steps:
        start = step['start']
        end = step['end']
        cost, path = a_star(numpad, start, end)
        print(f'numpad cost {cost}')
        for dir in path:
            if dir == 'down':
                numpad_directions += 'v'
            elif dir == 'right':
                numpad_directions += '>'
            elif dir == 'up':
                numpad_directions += '^'
            elif dir == 'left':
                numpad_directions += '<'
        numpad_directions += 'A'

    print(f'numpad_directions: {numpad_directions}')

    start = (0, 2)
    steps = []
    for code_piece in numpad_directions:
        movement = dict()
        movement['start'] = start
        for row in range(len(keypad)):
            for col in range(len(keypad[0])):
                if keypad[row][col] == code_piece:
                    end = (row, col)
                    movement['end'] = (row, col)
                    start = end
        if "end" not in movement:
            movement['end'] = start
        steps.append(movement)

    # print(steps)

    keypad_directions = ''
    for step in steps:
        # print(f'-------- step {step}')
        start = step['start']
        end = step['end']
        # print(start, end)
        cost, path = a_star(keypad, start, end)
        # print(f'cost {cost} --- path {path}')
        print(f'keypad one cost {cost}')
        for dir in path:
            if dir == 'down':
                keypad_directions += 'v'
            elif dir == 'right':
                keypad_directions += '>'
            elif dir == 'up':
                keypad_directions += '^'
            elif dir == 'left':
                keypad_directions += '<'
        keypad_directions += 'A'
        # print(f'keypad_directions after {keypad_directions}')

    print(f'keypad_directions: {keypad_directions}')

    start = (0, 2)
    steps = []
    for code_piece in keypad_directions:
        movement = dict()
        movement['start'] = start
        for row in range(len(keypad)):
            for col in range(len(keypad[0])):
                # print(numpad[row][col], code_piece)
                if keypad[row][col] == code_piece:
                    # print(f'code_piece is {code_piece}')
                    end = (row, col)
                    movement['end'] = (row, col)
                    start = end
        if "end" not in movement:
            movement['end'] = start
        steps.append(movement)

    print(steps)

    keypad_directions = ''
    for step in steps:
        # print(f'-------- step {step}')
        start = step['start']
        end = step['end']
        # print(start, end)
        cost, path = a_star(keypad, start, end)
        # print(f'cost {cost} --- path {path}')
        print(f'keypad 2 cost {cost}')
        for dir in path:
            if dir == 'down':
                keypad_directions += 'v'
            elif dir == 'right':
                keypad_directions += '>'
            elif dir == 'up':
                keypad_directions += '^'
            elif dir == 'left':
                keypad_directions += '<'
        keypad_directions += 'A'
        # print(f'keypad_directions after {keypad_directions}')

    print(f'keypad_directions: {keypad_directions}')

# figured out part 1 by hand first, but I'm stuck on how to programmatically calculate the best path for each next robot.
print(f'star1: {star1}')
print(f'star2: {star2}')