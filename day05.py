import os
import re
import copy

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47
# 75,47,61,53,29
# """


page_ordering = []
page_updates = []

ins = input.strip().split("\n\n")

for i in ins[0].strip().split('\n'):
    page_ordering.append(i.split('|'))

for i in ins[1].strip().split('\n'):
    page_updates.append(i.split(','))

valid_updates = []
invalid_updates = []

for page_update in page_updates:
    ruleBroken = False
    for rule in page_ordering:
        before = rule[0].strip()
        after = rule[1].strip()

        before_index = -1
        try:
            before_index = page_update.index(before)
        except ValueError:
            pass

        after_index = -1
        try:
            after_index = page_update.index(after)
        except ValueError:
            pass

        if before_index != -1 and after_index != -1:
            if before_index < after_index:
                pass
            else:
                ruleBroken = True
                break
    if not ruleBroken:
        valid_updates.append(page_update)
    else:
        invalid_updates.append(page_update)

for valid_update in valid_updates:
    star1 += int(valid_update[len(valid_update) // 2])

newly_valid_updates = []
for invalid_update in invalid_updates:

    foundSwaps = 999
    while(foundSwaps > 0):
        for rule in page_ordering:
            before = rule[0].strip()
            after = rule[1].strip()

            before_index = -1
            try:
                before_index = invalid_update.index(before)
            except ValueError:
                pass

            after_index = -1
            try:
                after_index = invalid_update.index(after)
            except ValueError:
                pass

            if before_index == -1 or after_index == -1:
                pass
            else:
                if before_index < after_index:
                    foundSwaps -= 1
                    pass
                else:
                    new_ordering = invalid_update[:after_index] + [invalid_update[before_index]] + invalid_update[after_index:before_index] + invalid_update[before_index+1:]
                    invalid_update = [i for i in new_ordering]
    newly_valid_updates.append(invalid_update)

for newly_valid_update in newly_valid_updates:
    star2 += int(newly_valid_update[len(newly_valid_update) // 2])

print(f'star1: {star1}')
print(f'star2: {star2}')