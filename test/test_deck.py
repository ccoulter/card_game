import unittest

from card_game.color import RED, GREEN, YELLOW
from card_game.card import Card
from card_game.deck import Deck
from card_game.hand import Hand
from card_game.shuffler import Shuffler


class Test(unittest.TestCase):

    """Some tests run with a mocked random number generator in order
    to shuffle the deck so the order of the cards in the shuffled
    deck is known -- allowing the dealt hands to be predictable
    for the unit tests to be successful.
    """

    def setUp(self):

        self.shuffler = Shuffler(0.5)

    ############################################################
    def testDeckCreateUnshuffled(self):
        """
        Create a default deck, validate the number of cards and point total.
        """

        deck = Deck.initialize_deck()
        self.assertEqual(39, len(deck))
        self.assertEqual(624, sum([card.point_value for card in deck]))

        hand = Hand()
        for _ in range(len(deck)):
            hand.add_card(deck.deal_card())

        self.assertEqual(0, len(deck))
        self.assertEqual(624, hand.score)

    def testDeckCreateShuffled(self):
        """
        Create a default deck, shuffle, and validate the cards were shuffled,
        the number of cards and point total.
        """

        deck = Deck.initialize_deck()
        original_cards = [c for c in deck]

        self.assertEqual(39, len(deck))
        self.assertEqual(624, sum([card.point_value for card in deck]))

        deck.shuffle()
        shuffled_cards = [c for c in deck]

        self.assertEqual(39, len(deck))
        self.assertEqual(624, sum([card.point_value for card in deck]))

        self.assertNotEquals(original_cards, shuffled_cards)

        hand = Hand()
        for _ in range(len(deck)):
            hand.add_card(deck.deal_card())

        self.assertEqual(0, len(deck))
        self.assertEqual(624, hand.score)
        self.assertEquals(shuffled_cards, hand.cards)

    def testDeckCreateShuffled1(self):
        """
        Create a default deck, shuffle, and validate the cards were shuffled,
        the number of cards and point total.
        """

        deck = Deck.initialize_deck_and_shuffle()
        shuffled_cards = [c for c in deck]

        self.assertEqual(39, len(deck))
        self.assertEqual(624, sum([card.point_value for card in deck]))

        hand = Hand()
        for _ in range(len(deck)):
            hand.add_card(deck.deal_card())

        self.assertEqual(0, len(deck))
        self.assertEqual(624, hand.score)
        self.assertEquals(shuffled_cards, hand.cards)

    def testDeckCreateShuffled2(self):
        """
        Create a default deck, shuffle, and validate the cards were shuffled,
        the number of cards and point total.
        """

        deck = Deck.initialize_deck_and_shuffle(num_shuffles=2)
        shuffled_cards = [c for c in deck]

        self.assertEqual(39, len(deck))
        self.assertEqual(624, sum([card.point_value for card in deck]))

        hand = Hand()
        for _ in range(len(deck)):
            hand.add_card(deck.deal_card())

        self.assertEqual(0, len(deck))
        self.assertEqual(624, hand.score)
        self.assertEquals(shuffled_cards, hand.cards)

    def testDeckCreateShuffled3(self):
        """
        Create a default deck, shuffle, and validate the cards were shuffled,
        the number of cards and point total.
        """

        deck = Deck.initialize_deck_and_shuffle(num_shuffles=3)
        shuffled_cards = [c for c in deck]

        self.assertEqual(39, len(deck))
        self.assertEqual(624, sum([card.point_value for card in deck]))

        hand = Hand()
        for _ in range(len(deck)):
            hand.add_card(deck.deal_card())

        self.assertEqual(0, len(deck))
        self.assertEqual(624, hand.score)
        self.assertEquals(shuffled_cards, hand.cards)

    def testDeckCreateMockShuffled1(self):
        """
        Create a default deck, do modified shuffle (repeatable), and validate the number of cards
        and point total.  Then redo and compare the resulting order of cards from both excercises.

        The above is executed for a list of shuffle modification factors to insure the modified
        shuffle operation is indeed repeatable over a wide range of values.
        """

        for factor_value in (
            0.0638,
            0.1,
            0.148,
            0.2,
            0.23,
            0.314,
            0.4374,
            0.5,
            0.627,
            0.873,
            0.9177,
        ):
            with self.subTest(factor=factor_value):
                deck = Deck.initialize_deck()
                deck.shuffler = Shuffler(factor_value)
                deck.shuffle()
                self.assertEqual(39, len(deck))
                self.assertEqual(624, sum([card.point_value for card in deck]))
                self.assertEqual(deck, deck)

                cards_from_prev_shuffle = [c for c in deck]

                deck = Deck.initialize_deck()
                deck.shuffler = Shuffler(factor_value)
                deck.shuffle()
                self.assertEqual(deck.cards, cards_from_prev_shuffle)

                deck = Deck.initialize_deck()
                deck.shuffler = Shuffler(factor_value)
                deck.shuffle()
                self.assertEqual(deck.cards, cards_from_prev_shuffle)

    ############################################################
    def testDeckOneHandMockDeal1(self):
        """
        Create a new deck, shuffle, deal all cards, validate
        number of cards and point total.
        """

        deck = Deck.initialize_deck()
        deck.shuffler = self.shuffler
        deck.shuffle()

        self.assertEqual(39, len(deck))
        self.assertEqual(624, sum([card.point_value for card in deck]))

        hand = Hand()
        for _ in range(len(deck)):
            hand.add_card(deck.deal_card())

        self.assertEqual(0, len(deck))
        self.assertEqual(624, hand.score)

    def testDeckOneHandMockDeal2(self):
        """
        Create a new deck, shuffle, deal 5 cards to a single hand.
        Validate number of cards and point total.
        Deal 2 more cards from same deck into same hand.
        Validate new number of cards and point total.
        Deal 15 more cards from same deck into same hand.
        Validate new number of cards and point total.
        """

        deck = Deck.initialize_deck()
        deck.shuffler = self.shuffler
        deck.shuffle()

        hand = Hand()
        for _ in range(5):
            hand.add_card(deck.deal_card())

        self.assertEqual(34, len(deck))

        self.assertEqual(5, len(hand))
        self.assertEqual(64, hand.score)

        for _ in range(2):
            hand.add_card(deck.deal_card())

        self.assertEqual(32, len(deck))

        self.assertEqual(7, len(hand))
        self.assertEqual(99, hand.score)

        for _ in range(15):
            hand.add_card(deck.deal_card())

        self.assertEqual(17, len(deck))

        self.assertEqual(22, len(hand))
        self.assertEqual(391, hand.score)

    ############################################################
    def testDeckTwoHandsMockDeal1(self):
        """
        Shuffle a clean deck twice, deal 3 hands,
        validate number of cards, score, and winner.

        Tests run with a mocked random number generator
        """

        deck = Deck.initialize_deck()
        deck.shuffler = self.shuffler
        deck.shuffle()

        ## regular deck
        self.assertEqual(39, len(deck))

        ## Deal 2 hands, 3 cards each
        hand1 = Hand("Player 1")
        hand2 = Hand("Player 2")

        hand1.add_card(deck.deal_card())
        hand2.add_card(deck.deal_card())
        hand1.add_card(deck.deal_card())
        hand2.add_card(deck.deal_card())
        hand1.add_card(deck.deal_card())
        hand2.add_card(deck.deal_card())

        self.assertEqual(33, len(deck))

        self.assertEqual(3, len(hand1))
        self.assertEqual(3, len(hand2))

        self.assertEqual(27, hand1.score)
        self.assertEqual(57, hand2.score)

        n, hands = Hand.determine_winner([hand1, hand2])
        self.assertEqual(1, n)
        self.assertEqual(1, len(hands))
        self.assertEqual(57, hands[0].score)

    def testDeckTwoHandsMockDeal2(self):
        """
        Shuffle a clean deck, deal 2 hands,
        validate number of cards, score, and winner.

        Tests run with a mocked random number generator
        """

        deck = Deck.initialize_deck()
        deck.shuffler = self.shuffler
        deck.shuffle()

        ## regular deck
        self.assertEqual(39, len(deck))

        ## Deal 2 hands, 3 cards each
        hand1, hand2 = deck.deal_hands(2, 3)

        self.assertEqual(33, len(deck))

        self.assertEqual(3, len(hand1))
        self.assertEqual(3, len(hand2))

        self.assertEqual(27, hand1.score)
        self.assertEqual(57, hand2.score)

        n, hands = Hand.determine_winner([hand1, hand2])
        self.assertEqual(1, n)
        self.assertEqual(1, len(hands))
        self.assertEqual(57, hands[0].score)

    def testDeckTwoHandsMockDeal3(self):
        """
        Shuffle a clean deck twice, deal 2 hands,
        validate number of cards, score, and winner.

        Tests run with a mocked random number generator
        """

        deck = Deck.initialize_deck(num_cards=20, colors=[RED])
        deck.shuffler = Shuffler(0.3972)

        deck.shuffle()
        self.assertEqual(20, len(deck))

        deck.shuffle()
        self.assertEqual(20, len(deck))

        hand1 = Hand()
        hand2 = Hand()

        hand1.add_card(deck.deal_card())
        hand2.add_card(deck.deal_card())
        hand1.add_card(deck.deal_card())
        hand2.add_card(deck.deal_card())
        hand1.add_card(deck.deal_card())
        hand2.add_card(deck.deal_card())

        self.assertEqual(3, len(hand1))
        self.assertEqual(3, len(hand2))

        self.assertEqual(111, hand1.score)
        self.assertEqual(135, hand2.score)

        self.assertFalse(hand1.is_winner(hand2))
        self.assertTrue(hand2.is_winner(hand1))

        n, winners = Hand.determine_winner([hand1, hand2])
        self.assertEqual(n, len(winners))
        self.assertEqual(1, len(winners))
        self.assertEqual(135, winners[0].score)

    def testDeckTwoHandsMockDeal4(self):
        """
        Shuffle a clean deck twice, deal 2 hands,
        validate number of cards, score, and winner.

        Tests run with a mocked random number generator
        """

        deck = Deck.initialize_deck(num_cards=20, colors=[RED])
        deck.shuffler = Shuffler(0.3972)

        deck.shuffle(2)
        self.assertEqual(20, len(deck))

        hand1 = Hand()
        hand2 = Hand()

        hand1.add_card(deck.deal_card())
        hand2.add_card(deck.deal_card())
        hand1.add_card(deck.deal_card())
        hand2.add_card(deck.deal_card())
        hand1.add_card(deck.deal_card())
        hand2.add_card(deck.deal_card())

        self.assertEqual(3, len(hand1))
        self.assertEqual(3, len(hand2))

        self.assertEqual(111, hand1.score)
        self.assertEqual(135, hand2.score)

        self.assertFalse(hand1.is_winner(hand2))
        self.assertTrue(hand2.is_winner(hand1))

        n, winners = Hand.determine_winner([hand1, hand2])
        self.assertEqual(n, len(winners))
        self.assertEqual(1, len(winners))
        self.assertEqual(135, winners[0].score)

    ############################################################
    def testDeckThreeHandsMockDeal1(self):
        """
        Shuffle a clean deck, deal 3 hands,
        validate number of cards, score, and winner.

        Tests run with a mocked random number generator
        """

        deck = Deck.initialize_deck()
        deck.shuffler = self.shuffler
        deck.shuffle()

        ## regular deck
        self.assertEqual(39, len(deck))

        ## Deal 3 hands, 3 cards each
        hand1, hand2, hand3 = deck.deal_hands(3, 3)

        self.assertEqual(30, len(deck))

        self.assertEqual(3, len(hand1))
        self.assertEqual(3, len(hand2))
        self.assertEqual(3, len(hand3))

        self.assertEqual(49, hand1.score)
        self.assertEqual(26, hand2.score)
        self.assertEqual(47, hand3.score)

        n, hands = Hand.determine_winner([hand1, hand2, hand3])
        self.assertEqual(1, n)
        self.assertEqual(1, len(hands))
        self.assertEqual(49, hands[0].score)

    def testDeckThreeHandsMockDeal2(self):
        """
        Shuffle a clean deck twice, deal 3 hands,
        validate number of cards, score, and winner.

        Tests run with a mocked random number generator
        """

        deck = Deck.initialize_deck(num_cards=20, colors=[RED])
        self.assertEqual(20, len(deck))

        deck.shuffler = Shuffler(0.3723)
        deck.shuffle()
        self.assertEqual(20, len(deck))

        hands = deck.deal_hands(num_hands=3, num_cards=5)
        self.assertEqual(3, len(hands))

        ordered_hands = Hand.sort_hands(hands)
        self.assertEqual(3, len(ordered_hands))

        scores = [hand.score for hand in ordered_hands]
        self.assertTrue(scores[0] > scores[1])
        self.assertTrue(scores[1] > scores[2])
        self.assertEqual([210, 174, 114], scores)

        n, winners = Hand.determine_winner(hands)
        self.assertEqual(1, n)
        self.assertEqual(1, len(winners))
        self.assertEqual(210, winners[0].score)

    ############################################################
    def testDeckEmpty(self):
        """
        Create a new deck, deal all cards, verify exception raised
        when deck is empty.
        """

        deck = Deck.initialize_deck()
        self.assertEqual(39, len(deck))
        self.assertEqual(624, sum([card.point_value for card in deck]))

        hand = Hand()
        for _ in range(len(deck)):
            hand.add_card(deck.deal_card())

        self.assertEqual(0, len(deck))

        with self.assertRaises(ValueError):
            card = deck.deal_card()

    ############################################################
    def testDeckSortThreeColors(self):

        deck = Deck()
        deck.add_cards(
            [
                Card(YELLOW, "K"),
                Card(RED, "J"),
                Card(GREEN, 6),
                Card(YELLOW, 5),
                Card(RED, 4),
                Card(GREEN, 2),
            ]
        )

        self.assertEqual(6, len(deck))
        self.assertNotEqual(1, len(deck))

        deck.shuffle()
        deck.sort_by_color([YELLOW.color, GREEN.color, RED.color])
        self.assertEqual(
            deck.cards,
            [
                Card(YELLOW, 5),
                Card(YELLOW, "K"),
                Card(GREEN, 2),
                Card(GREEN, 6),
                Card(RED, 4),
                Card(RED, "J"),
            ],
        )

        deck.shuffle()
        deck.sort_by_color([GREEN.color, YELLOW.color, RED.color])
        self.assertEqual(
            deck.cards,
            [
                Card(GREEN, 2),
                Card(GREEN, 6),
                Card(YELLOW, 5),
                Card(YELLOW, "K"),
                Card(RED, 4),
                Card(RED, "J"),
            ],
        )

        deck.shuffle()
        deck.sort_by_color([RED.color, GREEN.color, YELLOW.color])
        self.assertEqual(
            deck.cards,
            [
                Card(RED, 4),
                Card(RED, "J"),
                Card(GREEN, 2),
                Card(GREEN, 6),
                Card(YELLOW, 5),
                Card(YELLOW, "K"),
            ],
        )

    def testDeckSortTwoColors(self):

        deck = Deck()
        deck.add_cards(
            [
                Card(GREEN, 2),
                Card(GREEN, 6),
                Card(YELLOW, 5),
                Card(YELLOW, "K"),
                Card(RED, 4),
                Card(RED, "J"),
            ]
        )

        self.assertEqual(6, len(deck))
        self.assertNotEqual(1, len(deck))

        deck.shuffle()
        deck.sort_by_color([GREEN.color, RED.color])
        self.assertEqual(
            deck.cards,
            [
                Card(GREEN, 2),
                Card(GREEN, 6),
                Card(RED, 4),
                Card(RED, "J"),
                Card(YELLOW, 5),
                Card(YELLOW, "K"),
            ],
        )

        deck.shuffle()
        deck.sort_by_color([YELLOW.color, RED.color])
        self.assertEqual(
            deck.cards,
            [
                Card(YELLOW, 5),
                Card(YELLOW, "K"),
                Card(RED, 4),
                Card(RED, "J"),
                Card(GREEN, 2),
                Card(GREEN, 6),
            ],
        )

        deck.shuffle()
        deck.sort_by_color([GREEN.color, YELLOW.color])
        self.assertEqual(
            deck.cards,
            [
                Card(GREEN, 2),
                Card(GREEN, 6),
                Card(YELLOW, 5),
                Card(YELLOW, "K"),
                Card(RED, 4),
                Card(RED, "J"),
            ],
        )

    def testDeckSortSingleColor(self):

        deck = Deck()
        deck.add_cards(
            [
                Card(GREEN, 2),
                Card(GREEN, 6),
                Card(YELLOW, 5),
                Card(YELLOW, "K"),
                Card(RED, 4),
                Card(RED, "J"),
            ]
        )

        self.assertEqual(6, len(deck))
        self.assertNotEqual(1, len(deck))

        green_result = [
            Card(GREEN, 2),
            Card(GREEN, 6),
            Card(YELLOW, 5),
            Card(YELLOW, "K"),
            Card(RED, 4),
            Card(RED, "J"),
        ]

        deck.shuffle()
        deck.sort_by_color([GREEN.color])
        self.assertEqual(deck.cards, green_result)

        deck.shuffle()
        deck.sort_by_color(GREEN.color)
        self.assertEqual(deck.cards, green_result)

        red_result = [
            Card(RED, 4),
            Card(RED, "J"),
            Card(GREEN, 2),
            Card(GREEN, 6),
            Card(YELLOW, 5),
            Card(YELLOW, "K"),
        ]

        deck.shuffle()
        deck.sort_by_color([RED.color])
        self.assertEqual(deck.cards, red_result)

        deck.shuffle()
        deck.sort_by_color(RED.color)
        self.assertEqual(deck.cards, red_result)

        yellow_result = [
            Card(YELLOW, 5),
            Card(YELLOW, "K"),
            Card(GREEN, 2),
            Card(GREEN, 6),
            Card(RED, 4),
            Card(RED, "J"),
        ]

        deck.shuffle()
        deck.sort_by_color([YELLOW.color])
        self.assertEqual(deck.cards, yellow_result)

        deck.shuffle()
        deck.sort_by_color(YELLOW.color)
        self.assertEqual(deck.cards, yellow_result)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
