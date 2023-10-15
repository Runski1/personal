import random


def draw_card():
    card_value = random.randint(1, 13)
    if card_value == 1:
        card = "A"
        return card, 0
    elif 2 <= card_value <= 10:
        card = str(card_value)
        return card, card_value
    elif card_value == 11:
        card = "J"
        return card, 10
    elif card_value == 12:
        card = "Q"
        return card, 10
    elif card_value == 13:
        card = "K"
        return card, 10


def main():
    print("Play Blackjack")
    hand = []
    aces = 0
    hand_options = []
    hand_value = 0
    while True:
        user_input = input("Hit or Stay?").lower()
        if user_input == "h":
            card, card_value = draw_card()
            hand.append(card)
            if card_value != 0:
                if len(hand_options) == 0:
                    hand_options.append(card_value)
                else:
                    for h in hand_options:
                        h += card_value
            else:
                for h in hand_options:
                    h += 1
                hand_options.append( + 11)

