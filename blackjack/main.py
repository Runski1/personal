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


def hit(hand, hand_options):
    card, card_value = draw_card()
    print("Draw: " + card)
    hand.append(card)
    if card_value != 0:
        new_hand = []
        for value in hand_options:
            value += card_value
            new_hand.append(value)
        hand_options = new_hand
    else:
        new_hand = []
        for value in hand_options:
            value += 1
            new_hand.append(value)
            value += 10
            new_hand.append(value)
            hand_options = new_hand
    return hand, hand_options


def blackjack_checker(hand_options, who):
    new_hand = []
    for value in hand_options:
        if value == 21:
            if who == "player":
                print("Blackjack! You won!")
                exit()
            else:
                print("Dealer got blackjack. You lose.")
        if value < 21:
            new_hand.append(value)
    if len(new_hand) == 0:
        if who == "player":
            print("You busted!")
            exit()
        else:
            print("Dealer busted. You win!")
            exit()
    else:
        return new_hand


def dealers_turn(players_hand):
    hand = []
    possible_hands = [0]
    hand = []
    possible_hands = [0]
    for iterator in range(2):  # jakaa 2 ekaa korttia
        hand, possible_hands = hit(hand, possible_hands)
    while max(possible_hands) < players_hand:
        possible_hands = blackjack_checker(possible_hands, "dealer")
        print(hand, possible_hands)
        hand, possible_hands = hit(hand, possible_hands)
        possible_hands = blackjack_checker(possible_hands, "dealer")
    print("Dealer won with: " + ' '.join(hand) + " | value: " + str(max(possible_hands)))


def main():
    print("Play Blackjack")
    hand = []
    possible_hands = [0]
    for iterator in range(2):  # jakaa 2 ekaa korttia
        hand, possible_hands = hit(hand, possible_hands)
    while True:
        possible_hands = blackjack_checker(possible_hands, "player")
        print(hand, possible_hands)
        user_input = input("Hit or Stay?").lower()
        if user_input == "h":
            hand, possible_hands = hit(hand, possible_hands)
        else:
            print(max(possible_hands), type(max(possible_hands)))
            print("Your hand:" + ' '.join(hand) + "value: " + str(max(possible_hands)))
            dealers_turn(max(possible_hands))
            exit()


main()
