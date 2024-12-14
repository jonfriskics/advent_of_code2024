import os
import re
from PIL import Image
import numpy as np

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3
# """

# input = """
# p=2,4 v=2,-3
# """

def print_matrix(m):
    for l in range(len(m)):
        print(m[l])

matrix_width = 101
matrix_height = 103

# matrix_width = 11
# matrix_height = 7

matrix = []
for i in range(matrix_height):
    l = list()
    for j in range(matrix_width):
        l.append(0)
    matrix.append(l)

id = 1

robots = {}
for line in input.strip().split('\n'):
    matches = re.search(r'p=([-\d]+),([-\d]+)\s*v=([-\d]+),([-\d]+)', line)

    start_col = int(matches[1])
    start_row = int(matches[2])
    velocity_col = int(matches[3])
    velocity_row = int(matches[4])

    robots[id] = {}
    robots[id]['col'] = start_col
    robots[id]['row'] = start_row
    robots[id]['velocity_col'] = velocity_col
    robots[id]['velocity_row'] = velocity_row
    
    id += 1

iterations = 100

def find_new_position(pos, velocity, max_value):
    new_pos = pos + velocity
    if new_pos < 0:
        return max_value - abs(new_pos) % max_value
    return new_pos % max_value

def plot_points(mt, robots, matrix_width, matrix_height):
    for k, v in robots.items():
        mid_col = matrix_width // 2
        mid_row = matrix_height // 2

        if v['col'] == mid_col or v['row'] == mid_row:
            mt[v['row']][v['col']] = 0
        else:
            mt[v['row']][v['col']] = 255
    return mt

while iterations > 0:
    for k, v in robots.items():

        id = k
        col = v['col']
        row = v['row']
        velocity_col = v['velocity_col']
        velocity_row = v['velocity_row']

        new_col = 0
        new_row = 0

        new_col = find_new_position(col, velocity_col, matrix_width)
        new_row = find_new_position(row, velocity_row, matrix_height)

        robots[id]['col'] = new_col
        robots[id]['row'] = new_row

    # matrix = np.zeros((matrix_height, matrix_width), dtype=np.uint8)
    # m = plot_points(matrix, robots, matrix_width, matrix_height)
    # image = Image.fromarray(m, mode="L")
    # image.save(os.path.expanduser(f"~/code/day14/output_image_{iterations}.png"))
    iterations -= 1

quad1 = []
quad2 = []
quad3 = []
quad4 = []

for k, v in robots.items():
    robot = {k: (v['col'], v['row'])}

    mid_col = matrix_width // 2
    mid_row = matrix_height // 2

    if v['col'] == mid_col or v['row'] == mid_row:
        pass
    else:
        if v['col'] < mid_col and v['row'] < mid_row:
            quad1.append((v['col'],v['row']))
        elif v['col'] > mid_col and v['row'] < mid_row:
            quad2.append((v['col'],v['row']))
        elif v['col'] < mid_col and v['row'] > mid_row:
            quad3.append((v['col'],v['row']))
        elif v['col'] > mid_col and v['row'] > mid_row:
            quad4.append((v['col'],v['row']))

star1 = len(quad1) * len(quad2) * len(quad3) * len(quad4)

star2 = 'Set iterations to 10000, set matrix_width to 101 and matrix_height to 103, and uncomment the image.save() on lines 106 through 109 to export 10000 images!  Then count how many images it takes to see the xmas tree one and subtract that from 10000 + 1.  You will find the image at 2509, which means the answer is 10000 + 1 - 2509 = 7492'

print(f'star1: {star1}')
print(f'star2: {star2}')