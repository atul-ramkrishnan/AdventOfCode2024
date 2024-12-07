import re

with open('input.txt', 'r') as file:
    txt = file.read()
instructions = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", txt)
print(instructions)

res = 0

for instruction in instructions:
    num1 = int(instruction[instruction.find("(") + 1:instruction.find(",")])
    num2 = int(instruction[instruction.find(",") + 1:instruction.find(")")])
    res += num1 * num2

print(res)
