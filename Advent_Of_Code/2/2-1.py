import os


class Game:
    games = []
    id_sum = 0

    def __init__(self, id, draws):
        self.id = id
        self.draws = draws
        Game.games.append(self)

    def game_possible(self):
        for draw in self.draws:
            if draw.possible() is False:
                return False
        return True

    def find_power_of_min_cubes(self):
        min_red = 0
        min_blue = 0
        min_green = 0
        for draw in self.draws:
            if draw.reds > min_red:
                min_red = draw.reds
            if draw.blues > min_blue:
                min_blue = draw.blues
            if draw.greens > min_green:
                min_green = draw.greens
        power_of_cubes = min_red * min_blue * min_green
        return power_of_cubes
        # This might multiply with 0


class Draw:

    def __init__(self, greens, blues, reds):
        self.greens = greens
        self.blues = blues
        self.reds = reds

    def possible(self):
        if self.greens <= 13 and self.reds <= 12 and self.blues <= 14:
            return True
        else:
            return False


# file open and line parsing + object inits
with open(os.getcwd() + "/input.txt", "r") as file:
    for line in file:
        game_id = line.split(":")[0][5:]
        draws = line.split(":")[1].replace(" ", "").replace("\n", "").split(";")
        game_draws = []
        for draw in draws:
            greens = 0
            blues = 0
            reds = 0
            colors = draw.split(",")
            for color in colors:
                if color.find("green") > -1:
                    greens = int(color[0:-5])
                elif color.find("blue") > -1:
                    blues = int(color[0:-4])
                elif color.find("red") > -1:
                    reds = int(color[0:-3])
                else:
                    print("No color found???")
            game_draws.append(Draw(greens, blues, reds))
        Game(game_id, game_draws)

print("games: ", len(Game.games))
# count the games that are possible
id_count = 0
sum_of_power = 0
for game in Game.games:
    if game.game_possible() is True:
        id_count += int(game.id)
    sum_of_power += game.find_power_of_min_cubes()
print("id count: ", id_count)
print("sum of power: ", sum_of_power)
