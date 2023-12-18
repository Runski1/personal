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

# Now that we have a list of points where a symbol is located, we need to determine if a number is positioned
# adjacent to any of these symbols. I propose that we identify numbers, record the position of their first character,
# and note their length in characters. This information will allow us to calculate all adjacent points.
numberlist = []
with open(os.getcwd() + "/input.txt", "r") as file:
    for line_index, line in enumerate(file):
        for character_index, char in enumerate(line):
            numlength = 0
            i = 1
            number = ""
            if char.isdigit():
                numlength = 1
                number = char
                while True:
                    if line[character_index + i].isdigit():
                        numlength += 1
                        number += line[character_index + i]
                        i += 1
                    else:
                        break
                numberlist.append([int(number), (line_index, character_index), numlength])
# numberlist has lists [number, location_of_first_character, length]
# if there is a character in (character_index - 1) --- (character_index + (numlength -1)) range in
# lines (lineindex -1) --- (lineindex + 1), then number should be counted in the sum
print(numberlist)
