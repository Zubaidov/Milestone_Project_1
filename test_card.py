import unittest
from card_class import Card

class TestCard(unittest.TestCase):

    def test_one_class(self):
        suit = "Clubs"
        rank = "Three"
        three_of_clubs = Card(suit, rank)
        self.assertEqual(three_of_clubs, "Three of Clubs")

if __name__ == '__main__':
    unittest.main()