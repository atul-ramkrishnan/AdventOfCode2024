matrix = []

# Read the matrix from the file
with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(list(map(int, line.strip())))

# for line in matrix:
#     print(*line)


ROWS, COLS = len(matrix), len(matrix[0])
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_paths(i, j):
    if i < 0 or i >= ROWS or j < 0 or j >= COLS:
        return 0
    if matrix[i][j] == 9:
        return 1

    rc = 0
    for dir_x, dir_y in DIRECTIONS:
        nr, nc = i + dir_x, j + dir_y
        if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
            continue
        if matrix[nr][nc] == matrix[i][j] + 1:
            rc += get_paths(nr, nc)
    
    return rc

res = 0
for i in range(ROWS):
    for j in range(COLS):
        if matrix[i][j] == 0:
            res += get_paths(i, j)

print(res)
