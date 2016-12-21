import unittest
from display import Display
from bitarray import bitarray


class DisplayTests(unittest.TestCase):
    def test_simple_set(self):
        d = Display()
        self.assertEqual(bitarray("000000"), d.col[0])
        d.rect(1, 1)
        self.assertEquals(bitarray("100000"), d.col[0])
        d.rect(1, 2)
        self.assertEquals(bitarray("110000"), d.col[0])
        d.rect(1, 3)
        self.assertEquals(bitarray("111000"), d.col[0])
        d.rect(3, 3)
        self.assertEquals(bitarray("111000"), d.col[0])
        self.assertEquals(bitarray("111000"), d.col[1])
        self.assertEquals(bitarray("111000"), d.col[2])
        self.assertEquals(bitarray("000000"), d.col[3])

    def test_rotate_column(self):
        d = Display()
        d.rect(1, 3)
        d.rotate_column(0, 1)
        self.assertEqual(bitarray("011100"), d.col[0])
        d.rotate_column(0, 1)
        self.assertEqual(bitarray("001110"), d.col[0])
        d.rotate_column(0, 2)
        self.assertEqual(bitarray("100011"), d.col[0])

    def test_rotate_row(self):
        d = Display()
        d.rect(1, 3)
        self.assertEqual(bitarray("111000"), d.col[0])
        self.assertEqual(bitarray("000000"), d.col[1])
        d.rotate_row(0, 1)
        self.assertEqual(bitarray("011000"), d.col[0])
        self.assertEqual(bitarray("100000"), d.col[1])
        d.rotate_row(0, 2)
        self.assertEqual(bitarray("011000"), d.col[0])
        self.assertEqual(bitarray("000000"), d.col[1])
        self.assertEqual(bitarray("000000"), d.col[2])
        self.assertEqual(bitarray("100000"), d.col[3])

    def test_wraparound_column(self):
        d = Display()
        d.rect(1, 5)
        self.assertEqual(bitarray("111110"), d.col[0])
        d.rotate_column(0, 1)
        self.assertEqual(bitarray("011111"), d.col[0])
        d.rotate_column(0, 1)
        self.assertEqual(bitarray("101111"), d.col[0])

    def test_render(self):
        d = Display()
        d.rect(3, 3)
        self.assertRegexpMatches(d.render()[0], "###\.\.\..*")
        self.assertRegexpMatches(d.render()[1], "###\.\.\..*")
        self.assertRegexpMatches(d.render()[2], "###\.\.\..*")
        self.assertRegexpMatches(d.render()[3], "\.\.\..*")
        self.assertRegexpMatches(d.render()[4], "\.\.\..*")
        d.rotate_column(1, 1)
        self.assertRegexpMatches(d.render()[0], "#\.#\.\.\..*")
        self.assertRegexpMatches(d.render()[1], "###\.\.\..*")
        self.assertRegexpMatches(d.render()[2], "###\.\.\..*")
        self.assertRegexpMatches(d.render()[3], "\.#\..*")
        self.assertRegexpMatches(d.render()[4], "\.\.\..*")

    def test_parse(self):
        d = Display()
        d.parse(["rect 4x1",
                 "rotate row y=0 by 2",
                 "rotate column x=0 by 1"])
        self.assertEqual(bitarray("000000"), d.col[0])
        self.assertEqual(bitarray("000000"), d.col[1])
        self.assertEqual(bitarray("100000"), d.col[2])
        self.assertEqual(bitarray("100000"), d.col[3])
        self.assertEqual(bitarray("100000"), d.col[4])
        self.assertEqual(bitarray("100000"), d.col[5])

    def test_count_pixels(self):
        d = Display()
        self.assertEqual(0, d.count_pixels())
        d.rect(1, 3)
        self.assertEqual(3, d.count_pixels())
        d.rect(2, 2)
        self.assertEqual(5, d.count_pixels())
        d.rect(3, 3)
        self.assertEqual(9, d.count_pixels())
