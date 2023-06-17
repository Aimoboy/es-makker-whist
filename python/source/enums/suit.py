from enum import Enum

class Suit(Enum):
    Joker = 0,
    Clubs = 1,
    Diamonds = 2,
    Spades = 3,
    Hearts = 4

def suit_to_string(suit):
    if suit == Suit.Joker:
        return "Joker"
    elif suit == Suit.Clubs:
        return "Clubs"
    elif suit == Suit.Diamonds:
        return "Diamonds"
    elif suit == Suit.Spades:
        return "Spades"
    elif suit == Suit.Hearts:
        return "Hearts"
    else:
        return "Unknown"
