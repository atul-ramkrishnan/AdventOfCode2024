def concat(a, b):
    return int(str(a) + str(b))

def canSolveRec(arr, target, curr, i):
    if curr > target:
        return False
    if i == len(arr):
        return curr == target
    return canSolveRec(arr, target, curr + arr[i], i+1) or canSolveRec(arr, target, curr * arr[i], i+1) or canSolveRec(arr, target, concat(curr, arr[i]), i+1)

def canSolve(arr, target):
    return canSolveRec(arr, target, arr[0], 1)
res = 0
with open('input.txt', 'r') as file:
    for line in file:
        sep = line.find(':')
        target = int(line[:sep])
        arr = list(map(int, line[sep+1:].strip().split(' ')))
        res += (target if canSolve(arr, target) else 0)

print(res)

