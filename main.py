import random
from art import logo

# function to deal a random card


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# function to calculate the score


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
        # returning 0 for a 'blackjack'

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# lists to hold cards dealt for both user and computer
user_cards = []
computer_cards = []

# for loop to deal 2 cards each to both user and computer
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"     Your cards: {user_cards}, current score: {user_score}")
print(f"     Computer's first card: {computer_cards[0]}")
