import os
import re
import math

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# Register A: 0
# Register B: 0
# Register C: 9

# Program: 2,6
# """

# input = """
# Register A: 10
# Register B: 0
# Register C: 0

# Program: 5,0,5,1,5,4
# """

# input = """
# Register A: 0
# Register B: 0
# Register C: 0

# Program: 0,1,2,3
# """

# input = """
# Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0
# """

# input = """
# Register A: 117440
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0
# """

def run_program(register_a, register_b, register_c, program):
    matches = re.search(r'Register\sA:\s(\d+)\s*Register\sB:\s(\d+)\s*Register\sC:\s(\d+)\s*Program:\s([\d,]+)', input.strip())

    instruction_pointer = 0
    output = []

    def combo(operand, register_a, register_b, register_c):
        if operand <= 3:
            return operand
        elif operand == 4:
            return register_a
        elif operand == 5:
            return register_b
        elif operand == 6:
            return register_c
        elif operand == 7:
            print('7 received - program broken')
            exit()    

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer+1]

        if opcode == 0:
            # adv
            register_a = math.trunc(register_a / (2 ** combo(operand, register_a, register_b, register_c)))
        elif opcode == 1:
            # bxl
            register_b = register_b ^ operand
        elif opcode == 2:
            # bst
            register_b = combo(operand, register_a, register_b, register_c) % 8
        elif opcode == 3:
            # jnz
            if register_a == 0:
                pass
            else:
                instruction_pointer = operand - 2
        elif opcode == 4:
            # bxc
            register_b = register_b ^ register_c
        elif opcode == 5:
            # out
            output.append(combo(operand, register_a, register_b, register_c) % 8)
        elif opcode == 6:
            # bdv
            register_b = math.trunc(register_a / (2 ** combo(operand, register_a, register_b, register_c)))
        elif opcode == 7:
            # cdv
            register_c = math.trunc(register_a / (2 ** combo(operand, register_a, register_b, register_c)))

        instruction_pointer += 2
    return output

matches = re.search(r'Register\sA:\s(\d+)\s*Register\sB:\s(\d+)\s*Register\sC:\s(\d+)\s*Program:\s([\d,]+)', input.strip())
program = matches[4].split(',')
program = [int(x) for x in program]
register_a = int(matches[1])
register_b = int(matches[2])
register_c = int(matches[3])

output = run_program(register_a, register_b, register_c, program)

output = [str(x) for x in output]
star1 = ','.join(output)

# counter = 0
# while 1 == 1:
#     if counter != 30344604:
#         output = run_program(counter, register_b, register_c, program)
#         if counter % 10000000 == 0:
#             print(counter, output)
#         if output == program:
#             star2 = counter
#             break

#     counter += 1

print(f'star1: {star1}')
print(f'star2: {star2}')