"""
    Name: Deck
    Goal: encapsulate a list of cards that can be shuffled and dealt to a hand.

    Cards can be dealt (removed from the top of the deck)

    Multiple hands can be created, each receiving the same number of cards in turn.
"""

from __future__ import annotations
from typing import List

from .card import Card
from .cards import Cards
from .color import Color, DEFAULT_COLORS
from .hand import Hand
from .shuffler import Shuffler


class Deck(Cards):
    def __init__(self):
        Cards.__init__(self)
        self._shuffler = Shuffler()

    def deal_card(self) -> Card:
        """
        Remove the top card from the deck and return to caller.
        """
        card = self.pop()
        return card

    def deal_hands(self, num_hands: int = 2, num_cards: int = 3) -> List[Hand]:
        """
        Create the specified number of hands and then deal the specified
        number of cards, one at a time to each hand in sequence.
        """
        hands = [Hand("Player %d" % (n + 1)) for n in range(num_hands)]
        for _ in range(num_cards):
            for hand in hands:
                hand.add_card(self.deal_card())
        return hands

    def shuffle(self, num_shuffles: int = 1):
        self._shuffler.shuffle(self._cards, num_shuffles)

    @property
    def shuffler(self) -> Shuffler:
        return self._shuffler

    @shuffler.setter
    def shuffler(self, shuffler: Shuffler):
        self._shuffler = shuffler

    @staticmethod
    def initialize_deck(
        num_cards: int = 13, colors: List[Color] = DEFAULT_COLORS
    ) -> Deck:
        """
        Add the the specified number of cards (spot value from 2-nn)
        of the specified colors to the deck list.  The cards are loaded
        in color and spot value order.
        """

        min_value = 2  # lowest numbered card
        max_value = min_value + num_cards  # highest for range()
        deck = Deck()
        deck.add_cards(
            [Card(color, n) for color in colors for n in range(min_value, max_value)]
        )
        return deck

    @staticmethod
    def initialize_deck_and_shuffle(
        num_cards: int = 13, colors: List[Color] = DEFAULT_COLORS, num_shuffles: int = 1
    ) -> Deck:
        """
        Create a "new" deck of cards and then shuffle them.
        """

        deck = Deck.initialize_deck(num_cards, colors)
        deck.shuffle(num_shuffles)
        return deck
