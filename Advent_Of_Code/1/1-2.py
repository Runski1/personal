import os


cwd = os.getcwd()
input_nums = []
num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
with open(cwd + "/1_input.txt", "r") as input_file:
    for line in input_file:
        first_pos = float('inf')
        last_pos = -1
        a_pos = float('inf')
        b_pos = -1

        for key in num_dict:
            if line.find(key) > -1:
                if line.find(key) < first_pos:
                    first_pos = line.find(key)
                    firstnum = num_dict[key]
                if line.rfind(key) > last_pos:
                    last_pos = line.rfind(key)
                    lastnum = num_dict[key]
        for i, char in enumerate(line):
            if char.isdigit():
                a = str(char)
                a_pos = i
                break
        for i, char in enumerate(reversed(line)):
            if char.isdigit():
                b = str(char)
                b_pos = len(line) - i - 1
                break

        if first_pos < a_pos:
            if last_pos > b_pos:
                input_nums.append(str(firstnum) + str(lastnum))
            else:
                input_nums.append(str(firstnum) + b)
        else:
            if last_pos > b_pos:
                input_nums.append(a + str(lastnum))
            else:
                input_nums.append(a + b)
output_nums = 0
for num in input_nums:
    output_nums += int(num)
print("Sum of everything: ", output_nums)
