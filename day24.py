import os
import re

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# x00: 1
# x01: 1
# x02: 1
# y00: 0
# y01: 1
# y02: 0

# x00 AND y00 -> z00
# x01 XOR y01 -> z01
# x02 OR y02 -> z02
# """

# input = """
# x00: 1
# x01: 0
# x02: 1
# x03: 1
# x04: 0
# y00: 1
# y01: 1
# y02: 1
# y03: 1
# y04: 1

# ntg XOR fgs -> mjb
# y02 OR x01 -> tnw
# kwq OR kpj -> z05
# x00 OR x03 -> fst
# tgd XOR rvg -> z01
# vdt OR tnw -> bfw
# bfw AND frj -> z10
# ffh OR nrd -> bqk
# y00 AND y03 -> djm
# y03 OR y00 -> psh
# bqk OR frj -> z08
# tnw OR fst -> frj
# gnj AND tgd -> z11
# bfw XOR mjb -> z00
# x03 OR x00 -> vdt
# gnj AND wpb -> z02
# x04 AND y00 -> kjc
# djm OR pbm -> qhw
# nrd AND vdt -> hwm
# kjc AND fst -> rvg
# y04 OR y02 -> fgs
# y01 AND x02 -> pbm
# ntg OR kjc -> kwq
# psh XOR fgs -> tgd
# qhw XOR tgd -> z09
# pbm OR djm -> kpj
# x03 XOR y03 -> ffh
# x00 XOR y04 -> ntg
# bfw OR bqk -> z06
# nrd XOR fgs -> wpb
# frj XOR qhw -> z04
# bqk OR frj -> z07
# y03 OR x01 -> nrd
# hwm AND bqk -> z03
# tgd XOR rvg -> z12
# tnw OR pbm -> gnj
# """

one = input.strip().split('\n\n')[0]
two = input.strip().split('\n\n')[1]
inputs = dict()

for rule in one.strip().split('\n'):
    matches = re.search(r'(\w+)\:\s(\d)', rule)
    wire = matches[1]
    value = int(matches[2])
    inputs[wire] = value

available = set()
missing = set()

for rule in two.strip().split('\n'):
    matches = re.search(r'(\w+)\s(\w+)\s(\w+)\s\-\>\s(\w+)', rule)

    value1 = matches[1]
    operation = matches[2]
    value2 = matches[3]
    destination = matches[4]
    if value1 in inputs and value2 in inputs:
        available.add((value1, operation, value2, destination))
    else:
        missing.add((value1, operation, value2, destination))

while True:
    while available:
        w = available.pop()
        value1 = w[0]
        operation = w[1]
        value2 = w[2]
        destination = w[3]
        
        calculation = 0
        if operation == 'AND':
            calculation = inputs[value1] & inputs[value2]
        elif operation == 'OR':
            calculation = inputs[value1] | inputs[value2]
        elif operation == 'XOR':
            calculation = inputs[value1] ^ inputs[value2]

        inputs[destination] = calculation

    if len(missing) < 1:
        break

    for (value1, operation, value2, destination) in list(missing):
        if value1 in inputs and value2 in inputs:
            available.add((value1, operation, value2, destination))
            missing.remove((value1, operation, value2, destination))

inputs = dict(sorted(inputs.items()))

binary_string = ''
for k, v in inputs.items():
    if k[0] == 'z':
        binary_string += str(v)

star1 = int(binary_string[::-1], 2)

print(f'star1: {star1}')
print(f'star2: {star2}')