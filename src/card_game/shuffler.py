"""
    Name: Shuffler
    Goal: shuffles (randomly reorders) a list of items

    The Shuffler object is responsible for shuffling a list of cards.

    By default, the shuffle is random although it is possible to configure
    the shuffler to  perform repeatable shuffles on a known list of cards
    where each shuffle of the initial card list produces the same exact same
    sort sequence of card to be dealt.
"""

import random

from card_game.hand import Cards


class Shuffler:
    def __init__(self, value: float = None):
        self.random_value = value

    def shuffle(self, cards: Cards, num_shuffles: int = 1) -> None:

        value = self.random_value

        def rand_function() -> float:
            return value

        for _ in range(num_shuffles):
            random.shuffle(cards, rand_function if value else None)
