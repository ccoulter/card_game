import unittest

from card_game.color import Color, RED, GREEN, YELLOW


class Test(unittest.TestCase):
    def testColorRed(self):
        self.assertEqual(RED.color, "red")
        self.assertEqual(RED.point_multiplier, 3)
        self.assertEqual(str(RED), "red/3")

    def testColorYellow(self):
        self.assertEqual(YELLOW.color, "yellow")
        self.assertEqual(YELLOW.point_multiplier, 2)
        self.assertEqual(str(YELLOW), "yellow/2")

    def testColorGreen(self):
        self.assertEqual(GREEN.color, "green")
        self.assertEqual(GREEN.point_multiplier, 1)
        self.assertEqual(str(GREEN), "green/1")

    ############################################################
    def testColorSameColor(self):
        self.assertEqual(GREEN, GREEN)
        self.assertEqual(YELLOW, YELLOW)
        self.assertEqual(RED, RED)

    ############################################################
    def testColorIdentity(self):
        self.assertTrue(GREEN is GREEN)
        self.assertTrue(YELLOW is YELLOW)
        self.assertTrue(RED is RED)

        self.assertFalse(GREEN is not GREEN)
        self.assertFalse(YELLOW is not YELLOW)
        self.assertFalse(RED is not RED)

        self.assertTrue(GREEN is not YELLOW)
        self.assertTrue(YELLOW is not RED)
        self.assertTrue(RED is not GREEN)

        self.assertFalse(GREEN is YELLOW)
        self.assertFalse(YELLOW is RED)
        self.assertFalse(RED is GREEN)

    ############################################################
    def testColorDifferentColor(self):
        self.assertNotEqual(GREEN, Color(RED.color, GREEN.point_multiplier))
        self.assertNotEqual(GREEN, Color(YELLOW.color, GREEN.point_multiplier))

        self.assertNotEqual(YELLOW, Color(RED.color, YELLOW.point_multiplier))
        self.assertNotEqual(YELLOW, Color(GREEN.color, YELLOW.point_multiplier))

        self.assertNotEqual(RED, Color(YELLOW.color, RED.point_multiplier))
        self.assertNotEqual(RED, Color(GREEN.color, RED.point_multiplier))

    ############################################################
    def testColorDifferentPointMultiplier(self):
        self.assertNotEqual(GREEN, Color(GREEN.color, RED.point_multiplier))
        self.assertNotEqual(GREEN, Color(GREEN.color, YELLOW.point_multiplier))

        self.assertNotEqual(YELLOW, Color(YELLOW.color, RED.point_multiplier))
        self.assertNotEqual(YELLOW, Color(YELLOW.color, GREEN.point_multiplier))

        self.assertNotEqual(RED, Color(RED.color, YELLOW.point_multiplier))
        self.assertNotEqual(RED, Color(RED.color, GREEN.point_multiplier))

    ############################################################
    def testColorNotConditions(self):
        self.assertNotEqual(GREEN, RED)
        self.assertNotEqual(GREEN, YELLOW)

        self.assertNotEqual(YELLOW, GREEN)
        self.assertNotEqual(YELLOW, RED)

        self.assertNotEqual(RED, GREEN)
        self.assertNotEqual(RED, YELLOW)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
