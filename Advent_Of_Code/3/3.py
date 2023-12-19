import os
import re  # ooh fancy regex import

distinct_symbols = set()  # another fancy thingy
with open(os.getcwd() + "/input.txt", "r") as file:
    for line in file:
        symbols = re.sub(r'[0-9.]', '', line).replace("\n", "")
        for char in symbols:
            distinct_symbols.add(char)

possible_symbols = list(distinct_symbols)
print(possible_symbols)

symbol_positions = []
with open(os.getcwd() + "/input.txt", "r") as file:
    for line_index, line in enumerate(file):
        for character_index, char in enumerate(line):
            if char in possible_symbols:
                symbol_positions.append((line_index, character_index))
potential_gears = []
with open(os.getcwd() + "/input.txt", "r") as file:
    for line_index, line in enumerate(file):
        for character_index, char in enumerate(line):
            if char == "*":
                potential_gears.append((line_index, character_index))
# Now that we have a list of points where a symbol is located, we need to determine if a number is positioned
# adjacent to any of these symbols. I propose that we identify numbers, record the position of their first character,
# and note their length in characters. This information will allow us to calculate all adjacent points.
numberlist = []
with open(os.getcwd() + "/input.txt", "r") as file:
    for line_index, line in enumerate(file):
        skip_character = 1  # dirtyy
        i = 1
        for character_index, char in enumerate(line):
            if skip_character > 1:  # This part will skip remaining characters in multi-character number
                skip_character -= 1
                continue
            if char.isdigit():
                surrounding_points = []
                numlength = 1
                number = char
                while True:
                    if line[character_index + i].isdigit():
                        numlength += 1
                        number += line[character_index + i]
                        skip_character += 1
                        i += 1
                    else:
                        break
                # Let's add all points that surround the numbers.
                # It shouldn't matter that coordinates that are out of
                # range are added, since they don't excist in symbol_positions anyway
                for i in range(-1, 2):
                    for j in range(character_index - 1, character_index + numlength + 1):
                        surrounding_points.append((line_index + i, j))

                numberlist.append([int(number), (line_index, character_index), numlength, set(surrounding_points)])

total_sum = 0
for number in numberlist:
    if number[3] & set(symbol_positions):
        total_sum += number[0]
print("Total sum: ", total_sum)

sumof_gear_ratio = 0
for gear in potential_gears:
    part_count = 0
    gear_ratio = 1
    for number in numberlist:
        if gear in set(number[3]):
            part_count += 1
            gear_ratio *= number[0]
        if part_count > 2:
            part_count = 0
            break
    if part_count == 2:
        sumof_gear_ratio += gear_ratio

print("Sum of gear ratio: ", sumof_gear_ratio)
