"""
    Name: Color
    Goal: encapsulate color name text and its corresponding scoring weight.

    The color's scoring weight is multiplied with the card's spot
    value to determine the card's point value.
"""

from __future__ import annotations


class Color:
    def __init__(self, color: str, point_multiplier: int):
        self._color = color
        self._point_multiplier = point_multiplier

    @property
    def color(self) -> str:
        return self._color

    @property
    def point_multiplier(self) -> int:
        return self._point_multiplier

    def __eq__(self, other: Color) -> bool:
        return self is other or (
            self._color == other._color
            and self._point_multiplier == other._point_multiplier
        )

    def __repr__(self) -> str:
        return "%s/%d" % (self.color, self.point_multiplier)


## Standard colors
GREEN = Color("green", 1)
YELLOW = Color("yellow", 2)
RED = Color("red", 3)

DEFAULT_COLORS = (RED, YELLOW, GREEN)
