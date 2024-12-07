matrix = []

# Read the matrix from the file
with open('input.txt', 'r') as file:
    for line in file:
        matrix.append(list(line.strip()))

ROWS, COLS = len(matrix), len(matrix[0])

res = 0
for i in range(1, ROWS - 1):
    for j in range(1, COLS - 1):
        if matrix[i][j] == 'A':
            if ((matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S') or
                (matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M')) and \
               ((matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S') or
                (matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M')):
                res += 1

print(res)