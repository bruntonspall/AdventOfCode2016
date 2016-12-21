import unittest
import rle


class TestRLE(unittest.TestCase):
    def test_simple_rle(self):
        self.assertEquals("ADVENT", rle.decode("ADVENT"))
        self.assertEquals("ABBBBBC", rle.decode("A(1x5)BC"))
        self.assertEquals("XYZXYZXYZ", rle.decode("(3x3)XYZ"))
        self.assertEquals("ABCBCDEFEFG", rle.decode("A(2x2)BCD(2x2)EFG"))
        self.assertEquals("(1x3)A", rle.decode("(6x1)(1x3)A"))
        self.assertEquals("X(3x3)ABC(3x3)ABCY", rle.decode("X(8x2)(3x3)ABCY"))

    def test_len_rle(self):
        self.assertEquals(6, rle.decode_length("ADVENT"))
        self.assertEquals(7, rle.decode_length("A(1x5)BC"))
        self.assertEquals(9, rle.decode_length("(3x3)XYZ"))
        self.assertEquals(11, rle.decode_length("A(2x2)BCD(2x2)EFG"))
        self.assertEquals(20, rle.decode_length("X(8x2)(3x3)ABCY"))
        self.assertEquals(241920,
            rle.decode_length("(27x12)(20x12)(13x14)(7x10)(1x12)A"))
