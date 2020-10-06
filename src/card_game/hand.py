"""
    Name: Hand
    Goal: encapsulate a list of cards

    A card or a list of cards may be added to a hand.

    A card may be removed from the front of the list.

    The Cards object may be iterated - producing a sequence of Card objects

    The hand's current score is recalculated as card are added to the hand.

    Two hands can be compared to determine a winner, loser, or a tie.
"""

from __future__ import annotations
from functools import total_ordering
from typing import List, Tuple

from .card import Card
from .cards import Cards


@total_ordering
class Hand(Cards):
    def __init__(self, name=None):
        Cards.__init__(self)
        self._score = 0
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def score(self) -> int:
        return self._score

    def add_card(self, card: Card) -> None:
        Cards.add_card(self, card)
        self._score += card.point_value

    def add_cards(self, cards: List[Card]) -> None:
        Cards.add_cards(self, cards)
        self._score += sum([card.point_value for card in cards])

    def is_tie(self, other: Hand) -> bool:
        """A tie exists if this hand has the same score as the other hand."""
        if not self.same_number_of_cards(other):
            raise ValueError(
                "Hands have different number of cards - %s vs. %s" % (self, other)
            )
        return self.score == other.score

    def is_winner(self, other: Hand) -> bool:
        """A winner exists if this hand has a greater score as the other hand."""
        if not self.same_number_of_cards(other):
            raise ValueError(
                "Hands have different number of cards - %s vs. %s" % (self, other)
            )
        return self.score > other.score

    def is_loser(self, other: Hand) -> bool:
        """A winner exists if this hand has a lesser score as the other hand."""
        if not self.same_number_of_cards(other):
            raise ValueError(
                "Hands have different number of cards - %s vs. %s" % (self, other)
            )
        return self.score < other.score

    def report_hand(self):
        """
        Generate a multi-line text representation of the hand.
        Show player, number of cards, score, and the cards themselves.
        """
        text = (
            """
Hand: "%s"
      cards=%d, total points=%d
"""
            % (self.name, len(self), self.score)
            + self.report_cards()
        )
        return text

    def __eq__(self, other: Hand) -> bool:
        return self.is_tie(other)

    def __gt__(self, other: Hand) -> bool:
        return self.is_winner(other)

    def __lt__(self, other: Hand) -> bool:
        return self.is_loser(other)

    def __repr__(self) -> str:
        return 'Hand(name="%s", cards=%d, score=%d)' % (
            self.name or "",
            len(self),
            self._score,
        )

    @staticmethod
    def sort_hands(hands: List[Hand], ascending: bool = False) -> List[Hand]:
        """
        Sort the list of hands in ascending or descending (default) order
        based on the hand's point score.
        """

        factor = 1 if ascending is True else -1

        def make_key(hand: Hand):
            return factor * hand.score

        return sorted(hands, key=make_key)

    @staticmethod
    def determine_winner(hands: List[Hand]) -> Tuple(int, List[Hand]):
        """
        Determine the winner from the list of hands.  If there is no clear
        winner, then determine the sublist of hands that tie.

        The return values are a tuple consisting of the number of hands
        and the list of hands that denote the winner or tied hands.

        Return values may be:
        (1, [hand4]) -- denotes a winner
        (2, [hand3, hand1]) -- denotes a tie
        (3, [hand2, hand3, hand1]) -- denotes a tie
        """

        hands = Hand.sort_hands(hands)
        if hands[0].is_winner(hands[1]):
            hands = hands[:1]
        else:
            top_score = hands[0].score
            hands = [hand for hand in hands if hand.score == top_score]

        return len(hands), hands
