from typing import List
from ..enums.suit import Suit

class Card:
    def __init__(self, rank: int, suit: Suit):
        if (rank < 1 or rank > 13) and suit != Suit.Joker:
            raise Exception('Rank needs a rank in the interval [1:13] except if it is a Joker, got', rank)
        
        if suit == Suit.Joker and rank != 0:
            raise Exception('A Joker needs a rank of 0, got', rank)

        self.rank = rank
        self.suit = suit

def get_card_deck() -> List[Card]:
    res = []

    suits = [Suit.Clubs, Suit.Diamonds, Suit.Spades, Suit.Hearts]

    for suit in suits:
        for rank in range(1, 14):
            res.append(Card(rank, suit))
    
    for _ in range(3):
        res.append(Card(0, Suit.Joker))
    
    return res
