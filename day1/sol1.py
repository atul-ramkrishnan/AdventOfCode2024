
col1 = []
col2 = []
with open('input', 'r') as file:
    # Read each line in the file
    for line in file:
        # Print each line
        col1.append(int(line.split()[0]))
        col2.append(int(line.split()[1]))
print(col1[-1])
col1.sort()
col2.sort()

res = sum([abs(c1 - c2) for c1, c2 in zip(col1, col2)])
print(res)