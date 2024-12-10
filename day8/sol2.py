from fractions import Fraction
locations = []

with open('input.txt', 'r') as file:
    i = 0
    for line in file:
        line = list(line.strip())
        for j in range(len(line)):
            locations.append((i, j, line[j]))
        i += 1

def slope(x1, y1, x2, y2):
    if x2 == x1:  # Vertical line
        return float('inf')
    return Fraction(y2 - y1, x2 - x1)  # Exact slope as a fraction


antinode_set = set()
for antenna1 in locations:
    for antenna2 in locations:
        if antenna1[2] == antenna2[2] and antenna1[2] != '.' and antenna1 != antenna2:
            m = slope(antenna1[0], antenna1[1], antenna2[0], antenna2[1])

            for antinode in locations:
                if m == slope(antenna1[0], antenna1[1], antinode[0], antinode[1]):
                    antinode_set.add((antinode[0], antinode[1]))
        

print(len(antinode_set))