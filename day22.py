import os
import re
import math
import itertools

day = re.search(r'\d+', os.path.basename(__file__)).group()

with open(f'inputs/day{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# 1
# """

# input = """
# 1
# 10
# 100
# 2024
# """

# input = """
# 1
# 2
# 3
# 2024
# """

def mix(secret, number):
    return number ^ secret

def prune(secret):
    return secret % 16777216

all_secrets = []
for line in input.strip().split('\n'):
    secret = int(line)
    counter = 0
    prices = [int(str(secret)[-1])]
    diffs = dict()
    diffs[counter] = dict()
    diffs[counter]['price'] = int(str(secret)[-1])
    diffs[counter]['diff'] = None
    while counter < 2000:
        pruned = prune(mix(secret, secret * 64))
        pruned2 = prune(mix(pruned, math.floor(pruned / 32)))
        pruned3 = prune(mix(pruned2, pruned2 * 2048))
        secret = pruned3
        price = int(str(secret)[-1])
        prices.append(price)

        counter += 1
        diffs[counter] = dict()
        diffs[counter]['price'] = price
        if counter > 0:
            diffs[counter]['diff'] = price - diffs[counter-1]['price']
        else:
            diffs[counter]['diff'] = None
    
    star1 += secret
    all_secrets.append(diffs)

def find_price_for_sequence(data, diff_sequence):
    sequence_length = len(diff_sequence)
    for key in range(len(data) - sequence_length + 1):
        current_sequence = [data[i]['diff'] for i in range(key, key + sequence_length)]
        if current_sequence == diff_sequence:
            final_key = key + sequence_length - 1
            return data[final_key]['price']
    
    return None

permutations = list(itertools.product(range(-9, 10), repeat=4))
permutations = [list(p) for p in permutations]
print(f'Total permutations: {len(permutations)}')

total_bananas = 0

# print(all_secrets)
for permutation in permutations:
    print(permutation, total_bananas)
    totals = []
    for secret in all_secrets:
        price = find_price_for_sequence(secret, permutation)
        if price != None:
            totals.append(price)

    if sum(totals) > total_bananas:
        total_bananas = sum(totals)

star2 = total_bananas

print(f'star1: {star1}')
print(f'star2: {star2}')