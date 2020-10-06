import unittest

from card_game.card import Card
from card_game.color import RED, GREEN, YELLOW


class Test(unittest.TestCase):
    def testCardGreen(self):
        card = Card(GREEN, 2)
        self.assertEqual(card.color, GREEN)
        self.assertEqual(card.color.color, "green")
        self.assertEqual(card.value, 2)
        self.assertEqual(str(card), "green(2)")
        self.assertEqual(repr(card), "green(2) multiplier=1")
        self.assertEqual(card.color.point_multiplier, 1)
        self.assertEqual(card.point_value, 2)

    def testCardGreenJack(self):
        card = Card(GREEN, 11)
        self.assertEqual(card.color, GREEN)
        self.assertEqual(card.color.color, "green")
        self.assertEqual(card.value, 11)
        self.assertEqual(card.color.point_multiplier, 1)
        self.assertEqual(str(card), "green(J)")
        self.assertEqual(repr(card), "green(J) multiplier=1")
        self.assertEqual(card.point_value, 11)

    def testCardGreenQueen(self):
        card = Card(GREEN, 12)
        self.assertEqual(card.color, GREEN)
        self.assertEqual(card.color.color, "green")
        self.assertEqual(card.value, 12)
        self.assertEqual(card.color.point_multiplier, 1)
        self.assertEqual(str(card), "green(Q)")
        self.assertEqual(repr(card), "green(Q) multiplier=1")
        self.assertEqual(card.point_value, 12)

    def testCardGreenKing(self):
        card = Card(GREEN, 13)
        self.assertEqual(card.color, GREEN)
        self.assertEqual(card.color.color, "green")
        self.assertEqual(card.value, 13)
        self.assertEqual(card.color.point_multiplier, 1)
        self.assertEqual(str(card), "green(K)")
        self.assertEqual(repr(card), "green(K) multiplier=1")
        self.assertEqual(card.point_value, 13)

    def testCardGreenAce(self):
        card = Card(GREEN, 14)
        self.assertEqual(card.color, GREEN)
        self.assertEqual(card.color.color, "green")
        self.assertEqual(card.value, 14)
        self.assertEqual(card.color.point_multiplier, 1)
        self.assertEqual(str(card), "green(A)")
        self.assertEqual(repr(card), "green(A) multiplier=1")
        self.assertEqual(card.point_value, 14)

    ############################################################
    def testCardRedNumber(self):
        card = Card(RED, 8)
        self.assertEqual(card.color, RED)
        self.assertEqual(card.color.color, "red")
        self.assertEqual(card.value, 8)
        self.assertEqual(card.color.point_multiplier, 3)
        self.assertEqual(str(card), "red(8)")
        self.assertEqual(card.point_value, 24)

    def testCardRedJack(self):
        card = Card(RED, 11)
        self.assertEqual(card.color, RED)
        self.assertEqual(card.color.color, "red")
        self.assertEqual(card.value, 11)
        self.assertEqual(card.color.point_multiplier, 3)
        self.assertEqual(str(card), "red(J)")
        self.assertEqual(card.point_value, 33)

    def testCardRedQueen(self):
        card = Card(RED, 12)
        self.assertEqual(card.color, RED)
        self.assertEqual(card.color.color, "red")
        self.assertEqual(card.value, 12)
        self.assertEqual(card.color.point_multiplier, 3)
        self.assertEqual(str(card), "red(Q)")
        self.assertEqual(card.point_value, 36)

    def testCardRedKing(self):
        card = Card(RED, 13)
        self.assertEqual(card.color, RED)
        self.assertEqual(card.color.color, "red")
        self.assertEqual(card.value, 13)
        self.assertEqual(card.color.point_multiplier, 3)
        self.assertEqual(str(card), "red(K)")
        self.assertEqual(card.point_value, 39)

    def testCardRedAce(self):
        card = Card(RED, 14)
        self.assertEqual(card.color, RED)
        self.assertEqual(card.color.color, "red")
        self.assertEqual(card.value, 14)
        self.assertEqual(card.color.point_multiplier, 3)
        self.assertEqual(str(card), "red(A)")
        self.assertEqual(card.point_value, 42)

    ############################################################
    def testCardYellowNumber(self):
        card = Card(YELLOW, 1)
        self.assertEqual(card.color, YELLOW)
        self.assertEqual(card.color.color, "yellow")
        self.assertEqual(card.value, 1)
        self.assertEqual(card.color.point_multiplier, 2)
        self.assertEqual(str(card), "yellow(1)")
        self.assertEqual(card.point_value, 2)

    def testCardYellowJack(self):
        card = Card(YELLOW, 11)
        self.assertEqual(card.color, YELLOW)
        self.assertEqual(card.color.color, "yellow")
        self.assertEqual(card.value, 11)
        self.assertEqual(card.color.point_multiplier, 2)
        self.assertEqual(str(card), "yellow(J)")
        self.assertEqual(card.point_value, 22)

    def testCardYellowQueen(self):
        card = Card(YELLOW, 12)
        self.assertEqual(card.color, YELLOW)
        self.assertEqual(card.color.color, "yellow")
        self.assertEqual(card.value, 12)
        self.assertEqual(card.color.point_multiplier, 2)
        self.assertEqual(str(card), "yellow(Q)")
        self.assertEqual(card.point_value, 24)

    def testCardYellowKing(self):
        card = Card(YELLOW, 13)
        self.assertEqual(card.color, YELLOW)
        self.assertEqual(card.color.color, "yellow")
        self.assertEqual(card.value, 13)
        self.assertEqual(card.color.point_multiplier, 2)
        self.assertEqual(str(card), "yellow(K)")
        self.assertEqual(card.point_value, 26)

    def testCardYellowAce(self):
        card = Card(YELLOW, 14)
        self.assertEqual(card.color, YELLOW)
        self.assertEqual(card.color.color, "yellow")
        self.assertEqual(card.value, 14)
        self.assertEqual(card.color.point_multiplier, 2)
        self.assertEqual(str(card), "yellow(A)")
        self.assertEqual(card.point_value, 28)

    ############################################################
    def testCardStringValue(self):
        card = Card(YELLOW, "5")
        self.assertEqual(card.color, YELLOW)
        self.assertEqual(card.color.color, "yellow")
        self.assertEqual(card.value, 5)
        self.assertEqual(card.color.point_multiplier, 2)
        self.assertEqual(str(card), "yellow(5)")
        self.assertEqual(card.point_value, 10)

        card = Card(YELLOW, "10")
        self.assertEqual(card.color, YELLOW)
        self.assertEqual(card.color.color, "yellow")
        self.assertEqual(card.value, 10)
        self.assertEqual(card.color.point_multiplier, 2)
        self.assertEqual(str(card), "yellow(10)")
        self.assertEqual(card.point_value, 20)

        card = Card(YELLOW, "J")
        self.assertEqual(card.color, YELLOW)
        self.assertEqual(card.color.color, "yellow")
        self.assertEqual(card.value, 11)
        self.assertEqual(card.color.point_multiplier, 2)
        self.assertEqual(str(card), "yellow(J)")
        self.assertEqual(card.point_value, 22)

        card = Card(YELLOW, "Q")
        self.assertEqual(card.color, YELLOW)
        self.assertEqual(card.color.color, "yellow")
        self.assertEqual(card.value, 12)
        self.assertEqual(card.color.point_multiplier, 2)
        self.assertEqual(str(card), "yellow(Q)")
        self.assertEqual(card.point_value, 24)

        card = Card(YELLOW, "K")
        self.assertEqual(card.color, YELLOW)
        self.assertEqual(card.color.color, "yellow")
        self.assertEqual(card.value, 13)
        self.assertEqual(card.color.point_multiplier, 2)
        self.assertEqual(str(card), "yellow(K)")
        self.assertEqual(card.point_value, 26)

        card = Card(YELLOW, "A")
        self.assertEqual(card.color, YELLOW)
        self.assertEqual(card.color.color, "yellow")
        self.assertEqual(card.value, 14)
        self.assertEqual(card.color.point_multiplier, 2)
        self.assertEqual(str(card), "yellow(A)")
        self.assertEqual(card.point_value, 28)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
