"""
    Name: Cards
    Goal: encapsulate a list of Cards

    A card or a list of cards may be added to the object's list of cards.

    A card may be removed from the front of the list. An exception is raised
    if the list of cards is empty.

    The Cards object may be iterated - producing a sequence of Card objects
"""

from __future__ import annotations
from typing import List, Union

from .card import Card


class Cards:
    def __init__(self):
        self._cards = []

    @property
    def cards(self) -> List[Card]:
        return self._cards

    def pop(self) -> Card:
        """
        Remove a card from the front of the list and return to caller.
        A ValueError exception is thrown if there are not more cards.
        """
        if len(self._cards) == 0:
            raise ValueError("Deck is empty.")
        return self._cards.pop(0)

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def add_cards(self, cards: List[Card]) -> None:
        self._cards.extend(cards)

    def report_cards(self):
        """
        Generate a multi-line text representation of the cards.
        """
        text = "\n".join(
            [
                "%7d) %-10s  %2d points" % (n, card, card.point_value)
                for n, card in enumerate(self._cards, 1)
            ]
        )
        return text

    def same_number_of_cards(self, other: Cards) -> bool:
        return len(self) == len(other)

    def sort_by_color(self, colors: Union[str, List[str]]) -> None:
        """
        The order of the sort is determined by the name text of the color(s)
        passed to the function.

        If there are fewer colors in the sort specification than the list of
        cards contain, the remaining colors sort in descending order of the
        color's scoring weight after all of the specified colors are sorted
        in the proper order.
        """
        if isinstance(colors, str):
            colors = [colors]
        sort_order = {color: n for n, color in enumerate(colors, -100)}

        def make_key(card: Card):
            return (
                sort_order.get(card.color.color, card.color.point_multiplier),
                card.value,
            )

        self._cards.sort(key=make_key)

    def sort_by_points(self, ascending: bool = False) -> None:
        """
        Cards are sorted by their weighted point value.  By default, the
        order is descending value.
        """

        factor = 1 if ascending is True else -1

        def make_key(card: Card):
            return factor * card.point_value

        self._cards.sort(key=make_key)

    def __eq__(self, other):
        return self._cards == other._cards

    def __iter__(self):
        return iter(self._cards)

    def __len__(self) -> int:
        return len(self._cards)

    def __repr__(self) -> str:
        return "Cards(%d)" % len(self)
