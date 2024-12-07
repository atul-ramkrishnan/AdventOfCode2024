def checkLevel(levels):
    if len(levels) == 0 or len(levels) == 1:
        return 1
    asc = True if levels[0] < levels[1] else False
    for i in range(len(levels)-1):
        if asc and levels[i] > levels[i+1]:
            return 0
        if not asc and levels[i] < levels[i+1]:
            return 0
        if abs(levels[i+1] - levels[i]) == 0 or abs(levels[i+1] - levels[i]) > 3:
            return 0
    return 1

def checkLevelWithDampener(levels):
    for i in range(len(levels)):
        if checkLevel(levels[:i] + levels[i+1:]) == 1:
            return 1
    return 0

levels = []
res = 0
with open('input.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Print each line
        levels = [int(level) for level in line.split()]
        res += checkLevelWithDampener(levels)

print(res)