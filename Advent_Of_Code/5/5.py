import os
import sys

maps = []
with open(os.getcwd() + "/input.txt", "r") as file:
    lines = file.readlines()
    seeds = lines[0][7:].split()
    seeds = [int(seed) for seed in seeds]
    seed2soil = lines[3:39]
    seed2soil = [[int(num) for num in line.replace("\n", "").split()] for line in seed2soil]  # 0_0
    maps.append(seed2soil)
    soil2fertilizer = lines[41:65]
    soil2fertilizer = [[int(num) for num in line.replace("\n", "").split()] for line in soil2fertilizer]
    maps.append(soil2fertilizer)
    fertilizer2water = lines[67:101]
    fertilizer2water = [[int(num) for num in line.replace("\n", "").split()] for line in fertilizer2water]
    maps.append(fertilizer2water)
    water2light = lines[103:149]
    water2light = [[int(num) for num in line.replace("\n", "").split()] for line in water2light]
    maps.append(water2light)
    light2temp = lines[151:180]
    light2temp = [[int(num) for num in line.replace("\n", "").split()] for line in light2temp]
    maps.append(light2temp)
    temp2humidity = lines[182:212]
    temp2humidity = [[int(num) for num in line.replace("\n", "").split()] for line in temp2humidity]
    maps.append(temp2humidity)
    humidity2location = lines[214:252]
    humidity2location = [[int(num) for num in line.replace("\n", "").split()] for line in humidity2location]
    maps.append(humidity2location)


def seed_to_location(seed, seedmaps):
    for map in seedmaps:
        for row in map:
            if row[1] <= seed < row[1] + row[2]:
                seed = (seed - row[1]) + row[0]
                break
    return seed


def location_to_seed(location, seedmaps):
    for map in reversed(seedmaps):
        for row in map:
            if (location >= row[0]) and (location <= row[0] + row[2] - 1):
                location = location - row[0] + row[1]
    return location


locations = []
new_seeds = []
# This will not work, too many seeds
# for i, seed in enumerate(seeds):
#     if i % 2 == 0:
#         for j in range(seeds[i + 1]):
#             new_seeds.append(seed + 0)

# I need to reverse the algoritm and figure out closest matching seed.
inf_int = sys.maxsize
closest_location = inf_int
for row in humidity2location:
    if row[0] <= closest_location:
        closest_location = row[0]
        my_range = (closest_location, closest_location + row[2])

print(my_range)

for location in range(my_range[0], my_range[1]):
    closest_seed = location_to_seed(location, maps)
    
# print("Closest location is: ", min(locations))
# print("Closest seed is: ", closest_seed)
