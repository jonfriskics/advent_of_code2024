import os
import re
import itertools

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# 190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20
# """

# input = """
# 192: 17 8 14
# """

for line in input.strip().split('\n'):
    test_value = int(line.split(': ')[0])
    numbers = line.split(': ')[1].split(' ')
    numbers = [int(n) for n in numbers]

    possible_operations = list(itertools.product(['+','*'], repeat=len(numbers)-1))
    operations_set = {o for o in possible_operations}

    for operations in operations_set:
        current_value = 0
        for n in range(len(numbers)-1):
            if n == 0:
                if operations[n] == '+':
                    current_value += numbers[n] + numbers[n+1]
                elif operations[n] == '*':
                    current_value += numbers[n] * numbers[n+1]
            else:
                if operations[n] == '+':
                    current_value = current_value + numbers[n+1]
                elif operations[n] == '*':
                    current_value = current_value * numbers[n+1]

        if current_value == test_value:
            star1 += test_value
            break

for line in input.strip().split('\n'):
    test_value = int(line.split(': ')[0])
    numbers = line.split(': ')[1].split(' ')
    numbers = [int(n) for n in numbers]

    possible_operations = list(itertools.product(['+','*','||'], repeat=len(numbers)-1))
    operations_set = {o for o in possible_operations}

    for operations in operations_set:
        current_value = 0
        for n in range(len(numbers)-1):
            if n == 0:
                if operations[n] == '||':
                    current_value = int(str(numbers[n]) + str(numbers[n+1]))
                elif operations[n] == '+':
                    current_value += numbers[n] + numbers[n+1]
                elif operations[n] == '*':
                    current_value += numbers[n] * numbers[n+1]
            else:
                if operations[n] == '||':
                    current_value = int(str(current_value) + str(numbers[n+1]))
                elif operations[n] == '+':
                    current_value = current_value + numbers[n+1]
                elif operations[n] == '*':
                    current_value = current_value * numbers[n+1]

        if current_value == test_value:
            star2 += test_value
            break

print(f'star1: {star1}')
print(f'star2: {star2}')