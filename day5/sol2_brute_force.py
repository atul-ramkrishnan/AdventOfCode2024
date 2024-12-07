from collections import defaultdict
import itertools

after_map = defaultdict(set)

res = 0
with open('input.txt', 'r') as file:
    for line in file:
        if '|' in line:
            before, after = line.strip().split('|')
            after_map[before].add(after)

        elif ',' in line:
            updates = line.strip().split(',')
            n = len(updates)

            valid = True
            for i in range(n):
                for j in range(i):
                    if updates[j] in after_map[updates[i]]:
                        valid = False
                        break
                
            if not valid:
                for perm in itertools.permutations(updates):
                    valid = True
                    for i in range(n):
                        for j in range(i):
                            if perm[j] in after_map[perm[i]]:
                                valid = False
                                break
                    if valid:
                        res += int(perm[n // 2])

print(res)