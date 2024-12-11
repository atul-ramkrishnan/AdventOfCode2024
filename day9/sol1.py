num_list = []

with open('input.txt', 'r') as file:
    for line in file:
        num_list = list(map(int, line.strip()))

n = len(num_list)
left, right = 0, n - 1
left_id = 0
right_id = n // 2
if n % 2 == 0:
    right -= 1
res = 0
pos = 0
while left <= right:
    # file
    for i in range(num_list[left]):
        # print(f"Adding {pos} * {left_id}")
        res += pos * left_id
        pos += 1
    left += 1

    if left > right:
        break
    # free space
    while left <= right and num_list[left] > 0:
        moved = min(num_list[left], num_list[right])
        for i in range(moved):
            # print(f"Adding {pos} * {right_id}")
            res += pos * right_id
            pos += 1
        num_list[left] -= moved
        num_list[right] -= moved

        if num_list[right] == 0:
            right -= 2
            right_id -= 1
    left_id += 1
    left += 1


print(res)
