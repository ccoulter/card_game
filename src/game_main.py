"""
    Card Game

    Deck has 3 colors: red, yellow, and green

    Each color has 13 cards, values from 2 to 14 (11-14 aka Jack, Queen, King, Ace)

    Hands consist of 1  or more cards an are scored by multiplying the card's numeric
    value by the color's weight factor (red=2, yellow=2, green=1) and summing the products.

    A game consists of multiple hands consisting of the same number of cards in each.  The
    winning hand is the one with the highest score.  Ties of the highest score are possible.
"""

import sys
from typing import List

from card_game import Deck, Hand


def say(message: str = "\n"):
    """write the message to the terminal"""
    sys.stdout.write(message)


def input_number(prompt: str) -> int:
    """write the prompt to the terminal and wait for input of an integer value"""
    num = 0
    while True:
        answer = input(prompt).strip()
        if answer:
            try:
                num = int(answer)
                break
            except ValueError as _:
                say("Invalid numeric input.  Try again.\n\n")
    return num


def main(argv: List[str]) -> int:

    rc = 0

    num_hands = input_number("How many hands to deal (enter 0 to terminate)? ")
    if num_hands == 0:
        return rc
    num_cards = input_number("How many cards for each hand (enter 0 to terminate)? ")
    if num_cards == 0:
        return rc

    deck = Deck.initialize_deck_and_shuffle()

    hands = deck.deal_hands(num_hands, num_cards)

    say()
    for hand in hands:
        say(hand.report_hand())
        say()

    n, winners = Hand.determine_winner(hands)

    say()
    if n == 1:
        say(winners[0].name + " has the winning hand")
    else:
        say("Game ended in a tie by:\n")
        for hand in winners:
            say(" " + hand.name)

    say()
    return rc


if __name__ == "__main__":
    rc = main(sys.argv)
    sys.exit(rc)
