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

