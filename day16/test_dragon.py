import unittest
import dragon


class DragonTest(unittest.TestCase):
    def test_expand(self):
        self.assertEquals("10000011110010000111",
                          dragon.expand(20, "10000"))

    def test_checksum(self):
        self.assertEquals("01100",
                          dragon.checksum("10000011110010000111"))

    def test_with_input(self):
        self.assertEquals("10100011010101011",
                          dragon.checksum(
                            dragon.expand(272, "11100010111110100")))

    def test_with_input2(self):
        self.assertEquals("01010001101011001",
                          dragon.checksum(
                            dragon.expand(35651584, "11100010111110100")))
