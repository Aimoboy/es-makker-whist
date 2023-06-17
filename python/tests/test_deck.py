import unittest
from source.classes.card import get_card_deck
from source.enums.suit import Suit

class TestDeck(unittest.TestCase):
    def test_deck_creation(self):
        cards = get_card_deck()

        self.assertEqual(len(cards), 55)
        
        clubs_count = len([card for card in cards if card.suit == Suit.Clubs])
        diamonds_count = len([card for card in cards if card.suit == Suit.Diamonds])
        spades_count = len([card for card in cards if card.suit == Suit.Spades])
        hearts_count = len([card for card in cards if card.suit == Suit.Hearts])
        joker_count = len([card for card in cards if card.suit == Suit.Joker])

        self.assertEqual(clubs_count, 13)
        self.assertEqual(diamonds_count, 13)
        self.assertEqual(spades_count, 13)
        self.assertEqual(hearts_count, 13)
        self.assertEqual(joker_count, 3)
