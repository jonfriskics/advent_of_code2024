import os
import re

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# """

for line in input.strip().split('\n'):
    mul_matches = re.findall(r'mul\(\d+\,\d+\)', line)
    for match in mul_matches:
        groups = re.search(r'mul\((\d+),(\d+)\)', match)
        left = groups.group(1)
        right = groups.group(2)
        star1 += int(left) * int(right)

# input = """
# xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
# """

isDo = True
for line in input.strip().split('\n'):
    while(1):
        first_do = re.search(r'do\(\)', line)
        first_dont = re.search(r'don\'t\(\)', line)
        first_mul = re.search(r'mul\((\d+),(\d+)\)', line)

        first_do_start_position = 0
        first_dont_start_position = 0
        first_mul_start_position = 0
        if first_do:
            first_do_start_position = int(first_do.span()[0])
        else:
            first_do_start_position = len(line)

        if first_dont:
            first_dont_start_position = int(first_dont.span()[0])
        else:
            first_dont_start_position = len(line)

        if first_mul:
            first_mul_start_position = first_mul.span()[0]
        else:
            # no more muls
            break

        if not isDo:
            if first_do_start_position < first_mul_start_position:
                isDo = True

        if first_mul_start_position < first_dont_start_position:
            if isDo:
                groups = re.search(r'mul\((\d+),(\d+)\)', line)
                left = groups.group(1)
                right = groups.group(2)
                star2 += int(left) * int(right)
            line = line[first_mul.span()[1]:]
        else:
            isDo = False
            line = line[first_dont.span()[1]:]

print(f'star1: {star1}')
print(f'star2: {star2}')