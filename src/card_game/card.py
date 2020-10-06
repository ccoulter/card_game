"""
    Name: Card
    Goal: encapsulate a Color and a spot value

    If the card has a spot value between 11 and 14, the alternate
    designations of 'J", "Q', 'K' and 'A' may be used (for J=Jack,
    Q=Queen, K=King, and A=Ace (Ace is the high card as long as
    there aren't more than 13 cards in a color suite).

    The color's scoring weight is multiplied with the card's spot
    value to determine the card's point value.

"""

from __future__ import annotations
from typing import Union

from .color import Color

_TO_DISPLAY = {11: "J", 12: "Q", 13: "K", 14: "A"}
_TO_VALUE = {v: k for k, v in _TO_DISPLAY.items()}


class Card:
    def __init__(self, color: Color, value: Union[int, str]):
        self._color = color
        self._value = value
        if not isinstance(value, int):
            self._value = _TO_VALUE.get(value)
            if self._value is None:
                self._value = int(value)

    @property
    def color(self) -> Color:
        return self._color

    @property
    def value(self) -> int:
        return self._value

    @property
    def point_value(self) -> int:
        return self._value * self._color.point_multiplier

    def __eq__(self, other: Card) -> bool:
        return self._color == other._color and self._value == other._value

    def __repr__(self) -> str:
        return """%s multiplier=%d""" % (str(self), self.color.point_multiplier)

    def __str__(self) -> str:
        return """%s(%s)""" % (
            self._color.color,
            _TO_DISPLAY.get(self._value, self._value),
        )
