matrix = []

# Read the matrix from the file
with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(list(line.strip()))

ROWS, COLS = len(matrix), len(matrix[0])

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

init_x, init_y = -1, -1
for i in range(ROWS):
    for j in range(COLS):
        if matrix[i][j] == '^':
            matrix[i][j] = '.'
            init_x, init_y = i, j
            break


def isCycle(visited, cur_x, cur_y, direction):
    while True:
        if (cur_x, cur_y, direction) in visited:
            return True
        visited.add((cur_x, cur_y, direction))
        if cur_x + DIRECTIONS[direction][0] < 0 or cur_x + DIRECTIONS[direction][0] >= ROWS or cur_y + DIRECTIONS[direction][1] < 0 or cur_y + DIRECTIONS[direction][1] >= COLS:
            return False
        if matrix[cur_x + DIRECTIONS[direction][0]][cur_y + DIRECTIONS[direction][1]] == '#':
            direction = (direction + 1) % 4
        else:
            cur_x += DIRECTIONS[direction][0]
            cur_y += DIRECTIONS[direction][1]


res = 0
for i in range(ROWS):
    for j in range(COLS):
        if matrix[i][j] == '.' and (i, j) != (init_x, init_y):
            matrix[i][j] = '#'
            visited = set()
            if isCycle(visited, init_x, init_y, 0):
                res += 1
            matrix[i][j] = '.'


print(res)
