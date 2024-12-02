import os
import re

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

# input = """
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# """

star1 = 0
star2 = 0

def star1_check(numbers):
    fail_condition = False
    direction = None

    for n in range(len(numbers)):
        if n == len(numbers)-1:
            break

        if numbers[n] > numbers[n+1]:
            if direction == 'decreasing':
                pass
            elif direction == 'increasing':
                fail_condition = True
                break
            direction = 'decreasing'

            if(abs(numbers[n] - numbers[n+1]) <= 3):
                pass
            elif(abs(numbers[n] - numbers[n+1] > 3)):
                fail_condition = True
            else:
                fail_condition = True
        elif numbers[n] < numbers[n+1]:
            if direction == 'increasing':
                pass
            elif direction == 'decreasing':
                fail_condition = True
                break
            direction = 'increasing'

            if(abs(numbers[n] - numbers[n+1]) <= 3):
                pass
            elif(abs(numbers[n] - numbers[n+1] > 3)):
                fail_condition = True
            else:
                fail_condition = True
        elif numbers[n] == numbers[n+1]:
            fail_condition = True
    return fail_condition

def star2_check(numbers):
    fail_condition = None
    
    for n in range(len(numbers)):
        new_numbers = numbers[0:n] + numbers[n+1:len(numbers)]
        fail_condition = star1_check(new_numbers) and fail_condition

    return fail_condition

for line in input.strip().split('\n'):
    numbers = [int(x) for x in line.split(' ')]

    fc = star1_check(numbers)
    if fc == False:
        star1 += 1
    
    fc = star2_check(numbers)
    if fc == False:
        star2 += 1

print(f'star1: {star1}')
print(f'star2: {star2}')