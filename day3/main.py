import re

sum_pt_1 = 0
sum_pt_2 = 0
mul_values = True

def mul(x, y):
    return x * y

def do():
    global mul_values
    mul_values = True

def dont():
    global mul_values
    mul_values = False

with open("input.txt", "r") as file:
    instructions = re.findall("mul\(\d{1,3},\d{1,3}\)", file.read())
    for instruction in instructions:
        sum_pt_1 += eval(instruction)

print(f"Sum: {sum_pt_1}")

with open("input.txt", "r") as file:

    instructions = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", file.read())
    for instruction in instructions:
        if instruction == "don't()":
            instruction = "dont()"
        eval(instruction)
        if mul_values and "mul" in instruction:
            sum_pt_2 += eval(instruction)

print(f"Sum: {sum_pt_2}")