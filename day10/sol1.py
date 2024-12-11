matrix = []

# Read the matrix from the file
with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(list(map(int, line.strip())))

# for line in matrix:
#     print(*line)


ROWS, COLS = len(matrix), len(matrix[0])
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_paths(i, j, visited):
    if i < 0 or i >= ROWS or j < 0 or j >= COLS:
        return 0
    if matrix[i][j] == 9:
        if (i, j) in visited:
            return 0
        visited.add((i, j))
        return 1

    rc = 0
    for dir_x, dir_y in DIRECTIONS:
        nr, nc = i + dir_x, j + dir_y
        if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
            continue
        if matrix[nr][nc] == matrix[i][j] + 1:
            rc += get_paths(nr, nc, visited)
    
    return rc

res = 0
visited = set()
for i in range(ROWS):
    for j in range(COLS):
        if matrix[i][j] == 0:
            visited.clear()
            res += get_paths(i, j, visited)

print(res)
