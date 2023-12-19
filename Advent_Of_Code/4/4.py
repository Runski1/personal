import os


class Scratchcard:
    cards = []
    new_cards = []
    copied_cards = []

    def __init__(self, id, winning_numbers, your_numbers, first_init=False):
        self.id = id
        self.winning_numbers = winning_numbers
        self.your_numbers = your_numbers
        if not first_init:
            self.new_cards.append(self)
        else:
            self.cards.append(self)

    def count_winning_nums(self):
        winning_nums = self.winning_numbers.intersection(self.your_numbers)
        winning_number_count = len(winning_nums)
        return winning_number_count

    def count_points(self):
        winning_numbercount = self.count_winning_nums()
        if winning_numbercount == 0:
            points = 0
        else:
            points = 2 ** (self.count_winning_nums() - 1)
        return points

    def init_new_cards(self):
        if self.count_winning_nums() >= 1:
            for i in range(self.count_winning_nums()):
                try:
                    id = self.id + i + 1
                    win_nums = Scratchcard.cards[id - 1].winning_numbers
                    own_nums = Scratchcard.cards[id - 1].your_numbers
                    Scratchcard(id, win_nums, own_nums)
                except IndexError:
                    print("IndexError")
                    print("ID: ", self.id + i + 1)
                    continue


def parse_input_file():
    with open(os.getcwd() + "/input.txt", "r") as file:
        for line in file:
            scratchcard = line.split(":")
            game_id = int(scratchcard[0][4:].replace(" ", ""))
            number_sets = scratchcard[1].split("|")
            winning_set = set(int(num) for num in number_sets[0].split())
            your_set = set(int(num) for num in number_sets[1].split())
            Scratchcard(game_id, winning_set, your_set, True)  # what a bad function name for object init


def print_info():
    print("cards: ", len(Scratchcard.cards))
    print("new_cards: ", len(Scratchcard.new_cards))
    print("copied_cards: ", len(Scratchcard.copied_cards))


parse_input_file()
points_total = 0
for card in Scratchcard.cards:
    points_total += card.count_points()

print("Ln 67 After counting points")
print_info()

for card in Scratchcard.cards:
    card.init_new_cards()

print("LN 73 After first new card init")
print_info()

while True:
    Scratchcard.copied_cards = Scratchcard.new_cards
    Scratchcard.cards.extend(Scratchcard.new_cards)
    Scratchcard.new_cards = []
    print("Calculating")
    for card in Scratchcard.copied_cards:
        card.init_new_cards()
    if len(Scratchcard.new_cards) == 0:
        Scratchcard.copied_cards = []
        break


print("After looping the cards:")
print_info()

print("Total points: ", points_total)

print("Scratchcards.cards        : ", len(Scratchcard.cards))
print("Scratchcards.new_cards    : ", len(Scratchcard.new_cards))
print("Scratchcards.copied_cards : ", len(Scratchcard.copied_cards))
