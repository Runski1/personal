import os
cwd = os.getcwd()
print(cwd)
input_nums = []
num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
with open(cwd + "/1_input.txt", "r") as input_file:
    for line in input_file:
        for char in line:
            if char.isdigit():
                a = str(char)
                break
        for char in reversed(line):
            if char.isdigit():
                b = str(char)
                break
        input_nums.append(a + b)
output_nums = 0
for num in input_nums:
    output_nums += int(num)
print(output_nums)