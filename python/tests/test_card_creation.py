import unittest
from source.classes.card import Card
from source.enums.suit import Suit

class TestCardCreation(unittest.TestCase):
    def test_create_card(self):
        card = Card(5, Suit.Clubs)

        self.assertEqual(card.rank, 5)
        self.assertEqual(card.suit, Suit.Clubs)
    
    def test_create_card_lower_limit_rank(self):
        card = Card(1, Suit.Clubs)

        self.assertEqual(card.rank, 1)
        self.assertEqual(card.suit, Suit.Clubs)
    
    def test_create_card_upper_limit_rank(self):
        card = Card(13, Suit.Clubs)

        self.assertEqual(card.rank, 13)
        self.assertEqual(card.suit, Suit.Clubs)
    
    def test_create_card_low_rank_fail(self):
        with self.assertRaises(Exception):
            Card(0, Suit.Clubs)
    
    def test_create_card_high_rank_fail(self):
        with self.assertRaises(Exception):
            Card(14, Suit.Clubs)
    
    def test_create_joker(self):
        joker = Card(0, Suit.Joker)

        self.assertEqual(joker.rank, 0)
        self.assertEqual(joker.suit, Suit.Joker)
    
    def test_create_joker_wrong_rank(self):
        with self.assertRaises(Exception):
            Card(1, Suit.Joker)
