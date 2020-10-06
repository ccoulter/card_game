import unittest

from card_game.color import RED, YELLOW, GREEN
from card_game.card import Card
from card_game.cards import Cards


class Test(unittest.TestCase):

    ############################################################
    def testCardsRed(self):
        cards = Cards()
        cards.add_card(Card(RED, 4))
        cards.add_card(Card(RED, 5))
        cards.add_card(Card(RED, 6))
        self.assertEqual(3, len(cards))
        self.assertEqual(str(cards), "Cards(3)")

    def testCardsYellow(self):
        cards = Cards()
        cards.add_card(Card(YELLOW, 4))
        cards.add_card(Card(YELLOW, 5))
        cards.add_card(Card(YELLOW, 6))
        self.assertEqual(3, len(cards))
        self.assertEqual(str(cards), "Cards(3)")

    def testCardsGreen(self):
        cards = Cards()
        cards.add_card(Card(GREEN, 4))
        cards.add_card(Card(GREEN, 5))
        cards.add_card(Card(GREEN, 6))
        self.assertEqual(3, len(cards))
        self.assertEqual(str(cards), "Cards(3)")

    ############################################################
    def testCardsRed2(self):
        card_list = [
            Card(RED, 4),
            Card(RED, 5),
            Card(RED, 6),
            Card(RED, 7),
        ]
        cards = Cards()
        cards.add_cards(card_list)
        self.assertEqual(4, len(cards))
        self.assertEqual(str(cards), "Cards(4)")

    def testCardsYellow2(self):
        card_list = [
            Card(YELLOW, 4),
            Card(YELLOW, 5),
            Card(YELLOW, 6),
            Card(YELLOW, "A"),
        ]
        cards = Cards()
        cards.add_cards(card_list)
        self.assertEqual(4, len(cards))
        self.assertEqual(str(cards), "Cards(4)")

    def testCardsGreen2(self):
        card_list = [
            Card(GREEN, 4),
            Card(GREEN, 5),
            Card(GREEN, 6),
            Card(GREEN, "J"),
            Card(GREEN, "Q"),
            Card(GREEN, "K"),
        ]
        cards = Cards()
        cards.add_cards(card_list)
        self.assertEqual(6, len(cards))
        self.assertEqual(str(cards), "Cards(6)")

    ############################################################
    def testCardsMixed1(self):
        card_list = [
            Card(RED, 4),
            Card(YELLOW, 5),
            Card(GREEN, 6),
        ]
        cards = Cards()
        cards.add_cards(card_list)

        self.assertEqual(3, len(cards))
        self.assertNotEqual(1, len(cards))

    def testCardsMixed2(self):
        card_list = [
            Card(YELLOW, 4),
            Card(GREEN, 5),
            Card(RED, 6),
        ]

        cards = Cards()
        cards.add_cards(card_list)

        self.assertEqual(3, len(cards))
        self.assertNotEqual(1, len(cards))
        self.assertEqual(cards.cards, card_list)

        sorted_cards = [
            Card(RED, 6),
            Card(YELLOW, 4),
            Card(GREEN, 5),
        ]

        cards.sort_by_points()

        self.assertEqual(cards.cards, sorted_cards)

    def testCardsMixed3(self):
        card_list = [
            Card(GREEN, 4),
            Card(RED, 5),
            Card(YELLOW, 6),
        ]
        cards = Cards()
        cards.add_cards(card_list)

        self.assertEqual(3, len(cards))
        self.assertNotEqual(1, len(cards))

    ############################################################
    def testCardsReport(self):

        card_list = [
            Card(RED, 3),
            Card(YELLOW, 3),
            Card(GREEN, 4),
        ]

        cards = Cards()
        cards.add_cards(card_list)

        master_text = """\
      1) red(3)       9 points
      2) yellow(3)    6 points
      3) green(4)     4 points"""

        report_text = cards.report_cards()
        self.assertEqual(report_text, master_text)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
