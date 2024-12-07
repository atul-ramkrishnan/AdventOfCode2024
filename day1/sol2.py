from collections import Counter

col1 = []
col2 = []
with open('input', 'r') as file:
    # Read each line in the file
    for line in file:
        # Print each line
        col1.append(int(line.split()[0]))
        col2.append(int(line.split()[1]))

counter = Counter(col2)
res = 0
for c1 in col1:
    res += c1 * counter[c1]

print(res)