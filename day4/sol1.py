matrix = []

# Read the matrix from the file
with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(list(line.strip()))

toFind = 'XMAS'
ROWS, COLS = len(matrix), len(matrix[0])

# Directions for moving (8 possible)
DIRECTIONS = [
    (0, 1),   # Right
    (0, -1),  # Left
    (1, 0),   # Down
    (-1, 0),  # Up
    (1, 1),   # Down-right
    (-1, -1), # Up-left
    (1, -1),  # Down-left
    (-1, 1)   # Up-right
]

def dfs(i, j, curIndex, dir_x, dir_y):
    # If the entire word is matched, return True
    if curIndex == len(toFind):
        return True
    # Boundary and validity checks
    if i < 0 or i >= ROWS or j < 0 or j >= COLS or matrix[i][j] != toFind[curIndex]:
        return False

    # Move in the same direction
    return dfs(i + dir_x, j + dir_y, curIndex + 1, dir_x, dir_y)

# Count all occurrences of the word
res = 0
for i in range(ROWS):
    for j in range(COLS):
        if matrix[i][j] == toFind[0]:  # Start DFS from every occurrence of the first letter
            for dir_x, dir_y in DIRECTIONS:  # Try each direction
                if dfs(i, j, 0, dir_x, dir_y):  # Start with curIndex = 0 and fixed direction
                    res += 1

print(res)