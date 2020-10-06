import unittest

from card_game.color import RED, YELLOW, GREEN
from card_game.card import Card
from card_game.hand import Hand


class Test(unittest.TestCase):
    def testHandRed(self):
        hand = Hand("Player Red")
        hand.add_card(Card(RED, 4))
        hand.add_card(Card(RED, 5))
        hand.add_card(Card(RED, 6))
        self.assertEqual(45, hand.score)
        self.assertEqual(3, len(hand))
        self.assertEqual(str(hand), 'Hand(name="Player Red", cards=3, score=45)')
        self.assertEqual(repr(hand), 'Hand(name="Player Red", cards=3, score=45)')

    def testHandYellow(self):
        hand = Hand("Player Yellow")
        hand.add_card(Card(YELLOW, 4))
        hand.add_card(Card(YELLOW, 5))
        hand.add_card(Card(YELLOW, 6))
        self.assertEqual(30, hand.score)
        self.assertEqual(3, len(hand))
        self.assertEqual(str(hand), 'Hand(name="Player Yellow", cards=3, score=30)')
        self.assertEqual(repr(hand), 'Hand(name="Player Yellow", cards=3, score=30)')

    def testHandGreen(self):
        hand = Hand("Player Green")
        hand.add_card(Card(GREEN, 4))
        hand.add_card(Card(GREEN, 5))
        hand.add_card(Card(GREEN, 6))
        self.assertEqual(15, hand.score)
        self.assertEqual(3, len(hand))
        self.assertEqual(str(hand), 'Hand(name="Player Green", cards=3, score=15)')
        self.assertEqual(repr(hand), 'Hand(name="Player Green", cards=3, score=15)')

    ############################################################
    def testHandRed2(self):
        cards = [
            Card(RED, 4),
            Card(RED, 5),
            Card(RED, 6),
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(45, hand.score)
        self.assertEqual(3, len(hand))
        self.assertEqual(str(hand), 'Hand(name="", cards=3, score=45)')
        self.assertEqual(repr(hand), 'Hand(name="", cards=3, score=45)')

    def testHandYellow2(self):
        cards = [
            Card(YELLOW, 4),
            Card(YELLOW, 5),
            Card(YELLOW, 6),
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(30, hand.score)
        self.assertEqual(3, len(hand))
        self.assertEqual(str(hand), 'Hand(name="", cards=3, score=30)')
        self.assertEqual(repr(hand), 'Hand(name="", cards=3, score=30)')

    def testHandGreen2(self):
        cards = [
            Card(GREEN, 4),
            Card(GREEN, 5),
            Card(GREEN, 6),
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(15, hand.score)
        self.assertEqual(3, len(hand))
        self.assertEqual(str(hand), 'Hand(name="", cards=3, score=15)')
        self.assertEqual(repr(hand), 'Hand(name="", cards=3, score=15)')

    ############################################################
    def testHandMixed1(self):
        cards = [
            Card(RED, 4),
            Card(YELLOW, 5),
            Card(GREEN, 6),
        ]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(28, hand.score)
        self.assertEqual(3, len(hand))

        self.assertNotEqual(99, hand.score)
        self.assertNotEqual(1, len(hand))

    def testHandMixed2(self):
        cards = [
            Card(YELLOW, 4),
            Card(GREEN, 5),
            Card(RED, 6),
        ]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(31, hand.score)
        self.assertEqual(3, len(hand))

        self.assertNotEqual(99, hand.score)
        self.assertNotEqual(1, len(hand))

    def testHandMixed3(self):
        cards = [
            Card(GREEN, 4),
            Card(RED, 5),
            Card(YELLOW, 6),
        ]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(31, hand.score)
        self.assertEqual(3, len(hand))

        self.assertNotEqual(99, hand.score)
        self.assertNotEqual(1, len(hand))

    ############################################################
    def testHandsEqual(self):
        cards = [
            Card(RED, 2),
            Card(YELLOW, 4),
            Card(GREEN, 2),
        ]
        hand1 = Hand()
        hand1.add_cards(cards)

        self.assertEqual(16, hand1.score)
        self.assertEqual(3, len(hand1))

        self.assertNotEqual(99, hand1.score)
        self.assertNotEqual(1, len(hand1))

        cards = [
            Card(RED, 3),
            Card(YELLOW, 3),
            Card(GREEN, 1),
        ]
        hand2 = Hand()
        hand2.add_cards(cards)

        self.assertEqual(16, hand2.score)
        self.assertEqual(3, len(hand2))

        self.assertNotEqual(99, hand2.score)
        self.assertNotEqual(1, len(hand2))

        ##################################################
        self.assertEqual(hand1, hand2)
        self.assertTrue(hand1 == hand2)
        self.assertFalse(hand1 != hand2)
        self.assertTrue(hand1.is_tie(hand2))
        self.assertFalse(hand1.is_winner(hand2))
        self.assertFalse(hand1.is_loser(hand2))
        self.assertTrue(hand1.same_number_of_cards(hand2))
        self.assertTrue(hand2.same_number_of_cards(hand1))

        ## hands are a tie
        hands = [hand1, hand2]
        n, winners = Hand.determine_winner(hands)
        self.assertEqual(2, n)
        self.assertEqual(hands, winners)

    ############################################################
    def testHandsTwoWinner(self):

        cards = [
            Card(RED, 2),
            Card(YELLOW, 4),
            Card(GREEN, 3),
        ]
        hand1 = Hand()
        hand1.add_cards(cards)

        self.assertEqual(17, hand1.score)
        self.assertEqual(3, len(hand1))

        self.assertNotEqual(99, hand1.score)
        self.assertNotEqual(1, len(hand1))

        cards = [
            Card(RED, 3),
            Card(YELLOW, 3),
            Card(GREEN, 1),
        ]
        hand2 = Hand()
        hand2.add_cards(cards)

        self.assertEqual(16, hand2.score)
        self.assertEqual(3, len(hand2))

        self.assertNotEqual(99, hand2.score)
        self.assertNotEqual(1, len(hand2))

        ##################################################
        self.assertNotEqual(hand1, hand2)
        self.assertFalse(hand1 == hand2)
        self.assertTrue(hand1 != hand2)
        self.assertTrue(hand1 > hand2)
        self.assertFalse(hand1 < hand2)

        self.assertFalse(hand1.is_tie(hand2))

        self.assertTrue(hand1.same_number_of_cards(hand2))
        self.assertTrue(hand2.same_number_of_cards(hand1))

        n, winner = Hand.determine_winner([hand1, hand2])
        self.assertEqual(1, n)
        self.assertEqual(17, winner[0].score)

        hands = Hand.sort_hands([hand1, hand2])
        self.assertEqual(17, hands[0].score)
        self.assertEqual(16, hands[1].score)

        n, winner = Hand.determine_winner(hands)
        self.assertEqual(1, n)
        self.assertEqual(17, winner[0].score)

        hands = Hand.sort_hands([hand1, hand2], ascending=True)
        self.assertEqual(16, hands[0].score)
        self.assertEqual(17, hands[1].score)

        n, winner = Hand.determine_winner(hands)
        self.assertEqual(1, n)
        self.assertEqual(17, winner[0].score)

    ############################################################
    def testHandsThreeWinner(self):

        cards1 = [
            Card(RED, 2),
            Card(YELLOW, 4),
            Card(GREEN, 3),
        ]

        cards2 = [
            Card(RED, 3),
            Card(YELLOW, 3),
            Card(GREEN, 1),
        ]

        cards3 = [
            Card(RED, 1),
            Card(YELLOW, 6),
            Card(GREEN, 4),
        ]

        hand1 = Hand()
        hand1.add_cards(cards1)

        self.assertEqual(17, hand1.score)
        self.assertEqual(3, len(hand1))

        self.assertNotEqual(99, hand1.score)
        self.assertNotEqual(1, len(hand1))

        hand2 = Hand()
        hand2.add_cards(cards2)

        self.assertEqual(16, hand2.score)
        self.assertEqual(3, len(hand2))

        self.assertNotEqual(99, hand2.score)
        self.assertNotEqual(1, len(hand2))

        hand3 = Hand()
        hand3.add_cards(cards3)

        self.assertEqual(19, hand3.score)
        self.assertEqual(3, len(hand3))

        self.assertNotEqual(99, hand3.score)
        self.assertNotEqual(1, len(hand3))

        ##################################################
        self.assertFalse(hand1.is_tie(hand2))
        self.assertFalse(hand1.is_tie(hand3))
        self.assertFalse(hand2.is_tie(hand3))

        self.assertTrue(hand1 != hand2)
        self.assertFalse(hand1 == hand2)
        self.assertTrue(hand1 != hand3)
        self.assertFalse(hand1 == hand3)
        self.assertTrue(hand2 != hand3)
        self.assertFalse(hand2 == hand3)

        hands = [hand1, hand2, hand3]
        n, winner = Hand.determine_winner(hands)
        self.assertEqual(1, n)
        self.assertEqual(19, winner[0].score)

        hands = Hand.sort_hands(hands)
        self.assertEqual(19, hands[0].score)
        self.assertEqual(17, hands[1].score)
        self.assertEqual(16, hands[2].score)

        n, winner = Hand.determine_winner(hands)
        self.assertEqual(1, n)
        self.assertEqual(19, winner[0].score)

        hands = Hand.sort_hands(hands, ascending=True)
        self.assertEqual(16, hands[0].score)
        self.assertEqual(17, hands[1].score)
        self.assertEqual(19, hands[2].score)

        n, winner = Hand.determine_winner(hands)
        self.assertEqual(1, n)
        self.assertEqual(19, winner[0].score)

    ############################################################
    def testHandsThreeTieTwo(self):

        cards1 = [
            Card(RED, 2),
            Card(YELLOW, 4),
            Card(GREEN, 5),
        ]

        cards2 = [
            Card(RED, 3),
            Card(YELLOW, 3),
            Card(GREEN, 1),
        ]

        cards3 = [
            Card(RED, 1),
            Card(YELLOW, 6),
            Card(GREEN, 4),
        ]

        hand1 = Hand()
        hand1.add_cards(cards1)

        self.assertEqual(19, hand1.score)
        self.assertEqual(3, len(hand1))

        hand2 = Hand()
        hand2.add_cards(cards2)

        self.assertEqual(16, hand2.score)
        self.assertEqual(3, len(hand2))

        hand3 = Hand()
        hand3.add_cards(cards3)

        self.assertEqual(19, hand3.score)
        self.assertEqual(3, len(hand3))

        ##################################################
        self.assertFalse(hand1.is_tie(hand2))
        self.assertTrue(hand1.is_tie(hand3))
        self.assertFalse(hand2.is_tie(hand3))

        self.assertTrue(hand1 != hand2)
        self.assertFalse(hand1 == hand2)
        self.assertTrue(hand1 == hand3)
        self.assertFalse(hand1 != hand3)
        self.assertTrue(hand2 != hand3)
        self.assertFalse(hand2 == hand3)

        hands = [hand1, hand2, hand3]
        n, winner = Hand.determine_winner(hands)
        self.assertEqual(2, n)
        self.assertEqual(19, winner[0].score)
        self.assertEqual(19, winner[1].score)

        hands = Hand.sort_hands(hands)
        self.assertEqual(19, hands[0].score)
        self.assertEqual(19, hands[1].score)
        self.assertEqual(16, hands[2].score)

        n, winner = Hand.determine_winner(hands)
        self.assertEqual(2, n)
        self.assertEqual(19, winner[0].score)
        self.assertEqual(19, winner[1].score)

        hands = Hand.sort_hands(hands, ascending=True)
        self.assertEqual(16, hands[0].score)
        self.assertEqual(19, hands[1].score)
        self.assertEqual(19, hands[2].score)

        n, winner = Hand.determine_winner(hands)
        self.assertEqual(2, n)
        self.assertEqual(19, winner[0].score)
        self.assertEqual(19, winner[1].score)

    ############################################################
    def testHandsThreeTieThree(self):

        cards1 = [
            Card(RED, 2),
            Card(YELLOW, 4),
            Card(GREEN, 5),
        ]

        cards2 = [
            Card(RED, 4),
            Card(YELLOW, 3),
            Card(GREEN, 1),
        ]

        cards3 = [
            Card(RED, 1),
            Card(YELLOW, 6),
            Card(GREEN, 4),
        ]

        hand1 = Hand()
        hand1.add_cards(cards1)

        self.assertEqual(19, hand1.score)
        self.assertEqual(3, len(hand1))

        hand2 = Hand()
        hand2.add_cards(cards2)

        self.assertEqual(19, hand2.score)
        self.assertEqual(3, len(hand2))

        hand3 = Hand()
        hand3.add_cards(cards3)

        self.assertEqual(19, hand3.score)
        self.assertEqual(3, len(hand3))

        ##################################################
        self.assertTrue(hand1.is_tie(hand2))
        self.assertTrue(hand1.is_tie(hand3))
        self.assertTrue(hand2.is_tie(hand3))

        self.assertTrue(hand1 == hand2)
        self.assertFalse(hand1 != hand2)
        self.assertTrue(hand1 == hand3)
        self.assertFalse(hand1 != hand3)
        self.assertTrue(hand2 == hand3)
        self.assertFalse(hand2 != hand3)

        hands = [hand1, hand2, hand3]
        n, winner = Hand.determine_winner(hands)
        self.assertEqual(3, n)
        self.assertEqual(19, winner[0].score)
        self.assertEqual(19, winner[1].score)
        self.assertEqual(19, winner[2].score)

        hands = Hand.sort_hands(hands)
        self.assertEqual(19, hands[0].score)
        self.assertEqual(19, hands[1].score)
        self.assertEqual(19, hands[2].score)

        n, winner = Hand.determine_winner(hands)
        self.assertEqual(3, n)
        self.assertEqual(19, winner[0].score)
        self.assertEqual(19, winner[1].score)
        self.assertEqual(19, winner[2].score)

        hands = Hand.sort_hands(hands, ascending=True)
        self.assertEqual(19, hands[0].score)
        self.assertEqual(19, hands[1].score)
        self.assertEqual(19, hands[2].score)

        n, winner = Hand.determine_winner(hands)
        self.assertEqual(3, n)
        self.assertEqual(19, winner[0].score)
        self.assertEqual(19, winner[1].score)
        self.assertEqual(19, hands[2].score)

    ############################################################
    def testHandsDifferentNumCards(self):

        cards = [
            Card(RED, 2),
            Card(YELLOW, 4),
            Card(GREEN, 3),
            Card(GREEN, "J"),
        ]
        hand1 = Hand()
        hand1.add_cards(cards)

        self.assertEqual(28, hand1.score)
        self.assertEqual(4, len(hand1))

        self.assertNotEqual(99, hand1.score)
        self.assertNotEqual(1, len(hand1))

        cards = [
            Card(RED, 3),
            Card(YELLOW, 3),
            Card(GREEN, 4),
        ]
        hand2 = Hand()
        hand2.add_cards(cards)

        self.assertEqual(19, hand2.score)
        self.assertEqual(3, len(hand2))

        self.assertNotEqual(99, hand2.score)
        self.assertNotEqual(1, len(hand2))

        ##################################################
        self.assertFalse(hand1.same_number_of_cards(hand2))
        self.assertFalse(hand2.same_number_of_cards(hand1))

        with self.assertRaises(ValueError):
            self.assertTrue(hand1 == hand2)

        with self.assertRaises(ValueError):
            self.assertTrue(hand1 != hand2)

        with self.assertRaises(ValueError):
            self.assertNotEqual(hand1, hand2)

        with self.assertRaises(ValueError):
            self.assertFalse(hand1 == hand2)

        with self.assertRaises(ValueError):
            self.assertTrue(hand1 != hand2)

        with self.assertRaises(ValueError):
            self.assertFalse(hand1.is_tie(hand2))

        with self.assertRaises(ValueError):
            self.assertFalse(hand1.is_winner(hand2))

        with self.assertRaises(ValueError):
            self.assertTrue(hand1.is_loser(hand2))

    ############################################################
    def testHandReport(self):

        cards = [
            Card(RED, 3),
            Card(YELLOW, 3),
            Card(GREEN, 4),
        ]

        hand = Hand("Player")
        hand.add_cards(cards)

        master_text = """
Hand: "Player"
      cards=3, total points=19
      1) red(3)       9 points
      2) yellow(3)    6 points
      3) green(4)     4 points"""

        report_text = hand.report_hand()
        self.assertEqual(report_text, master_text)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
