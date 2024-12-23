import os
import re

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# kh-tc
# qp-kh
# de-cg
# ka-co
# yn-aq
# qp-ub
# cg-tb
# vc-aq
# tb-ka
# wh-tc
# yn-cg
# kh-ub
# ta-co
# de-co
# tc-td
# tb-wq
# wh-td
# ta-ka
# td-qp
# aq-cg
# wq-ub
# ub-vc
# de-ta
# wq-aq
# wq-vc
# wh-yn
# ka-de
# kh-ta
# co-tc
# wh-qp
# tb-vc
# td-yn
# """

computers = set()
connections = []
for line in input.strip().split('\n'):
    matches = re.search(r'(\w\w)-(\w\w)', line)
    one = matches[1]
    two = matches[2]
    computers.add(one)
    computers.add(two)
    connection = dict()
    connection[one] = two
    connections.append(connection)
    connection = dict()
    connection[two] = one
    connections.append(connection)

c = dict()
    
for computer in computers:
    c[computer] = []
    for connection in connections:
        for k, v in connection.items():
            if computer == k:
                c[computer].append(v)

groups = []
keys = list(c.keys())

for x in range(len(keys)):
    for y in range(x + 1, len(keys)):
        for z in range(y + 1, len(keys)):
            key1, key2, key3 = keys[x], keys[y], keys[z]
            if (key2 in c[key1] and key3 in c[key1] and key1 in c[key2] and key3 in c[key2] and key1 in c[key3] and key2 in c[key3]):
                groups.append([key1, key2, key3])

for group in groups:
    for comp in group:
        if comp[0] == 't':
            star1 += 1
            break

print(f'star1: {star1}')
print(f'star2: {star2}')