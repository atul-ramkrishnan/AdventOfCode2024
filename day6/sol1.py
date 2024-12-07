matrix = []

# Read the matrix from the file
with open('test.txt', 'r') as file:
    for line in file:
        matrix.append(list(line.strip()))

for lst in matrix:
    print(*lst)
print()
ROWS, COLS = len(matrix), len(matrix[0])

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cur_x, cur_y = -1, -1
for i in range(ROWS):
    for j in range(COLS):
        if matrix[i][j] == '^':
            matrix[i][j] = '.'
            cur_x, cur_y = i, j
            break


direction = 0
res = 0

while cur_x >= 0 and cur_x < ROWS and cur_y >= 0 and cur_y < COLS:
    if matrix[cur_x][cur_y] == '.':  
        matrix[cur_x][cur_y] = 'X'
        res += 1
    if cur_x + DIRECTIONS[direction][0] < 0 or cur_x + DIRECTIONS[direction][0] >= ROWS or cur_y + DIRECTIONS[direction][1] < 0 or cur_y + DIRECTIONS[direction][1] >= COLS:
        break
    if matrix[cur_x + DIRECTIONS[direction][0]][cur_y + DIRECTIONS[direction][1]] == '#':
        direction = (direction + 1) % 4
    else:
        cur_x += DIRECTIONS[direction][0]
        cur_y += DIRECTIONS[direction][1]

# for lst in matrix:
#     print(*lst)
print(res)

