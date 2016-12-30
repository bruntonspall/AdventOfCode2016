import unittest
import scramble


class ScrambleTest(unittest.TestCase):
    def test_swap(self):
        input = list("abcde")
        self.assertEquals(list("adcbe"), scramble.swap(input, 1, 3))
        input = list("abcde")
        self.assertEquals(list("abcde"), scramble.swap(input, 2, 2))

    def test_swap_letters(self):
        input = list("abcde")
        self.assertEquals(list("adcbe"), scramble.swap(input, "b", "d"))

    def test_rotate(self):
        input = list("abcde")
        self.assertEquals(list("bcdea"), scramble.rotate_left(input, 1))
        self.assertEquals(list("eabcd"), scramble.rotate_right(input, 1))
        self.assertEquals(list("cdeab"), scramble.rotate_left(input, 2))
        self.assertEquals(list("deabc"), scramble.rotate_right(input, 2))

    def test_rotate_letters(self):
        input = list("abcdefghi")
        self.assertEquals(list("ghiabcdef"), scramble.rotate(input, "c"))
        self.assertEquals(list("defghiabc"), scramble.rotate(input, "e"))

    def test_reverse(self):
        input = list("abcdefghi")
        self.assertEquals(list("abedcfghi"), scramble.reverse(input, 2, 4))
        self.assertEquals(list("abfedcghi"), scramble.reverse(input, 2, 5))

    def test_move(self):
        input = list("abcdefghi")
        self.assertEquals(list("abdecfghi"), scramble.move(input, 2, 4))
        input = list("abcdefghi")
        self.assertEquals(list("abdefcghi"), scramble.move(input, 2, 5))

    def test_sample(self):
        input = list("abcde")

        input = scramble.swap(input, 4, 0)
        self.assertEquals(list("ebcda"), input)

        input = scramble.swap(input, "d", "b")
        self.assertEquals(list("edcba"), input)

        input = scramble.reverse(input, 0, 4)
        self.assertEquals(list("abcde"), input)

        input = scramble.rotate_left(input, 1)
        self.assertEquals(list("bcdea"), input)

        input = scramble.move(input, 1, 4)
        self.assertEquals(list("bdeac"), input)

        input = scramble.move(input, 3, 0)
        self.assertEquals(list("abdec"), input)

        input = scramble.rotate(input, "b")
        self.assertEquals(list("ecabd"), input)

        input = scramble.rotate(input, "d")
        self.assertEquals(list("decab"), input)

    def test_parse(self):
        input = [
            "swap position 4 with position 0",
            "swap letter d with letter b",
            "reverse positions 0 through 4",
            "rotate left 1 step",
            "move position 1 to position 4",
            "move position 3 to position 0",
            "rotate based on position of letter b",
            "rotate based on position of letter d",
            "rotate right 2 steps",
        ]

        self.assertEquals("abdec", scramble.parse("abcde", input))

    def test_actual_input(self):
        lines = [line.strip() for line in open("input.txt")]
        self.assertEquals("aefgbcdh", scramble.parse("abcdefgh", lines))

    def test_revese_rotate(self):
        input = [
            "rotate based on position of letter b",
            "rotate based on position of letter d",
        ]
        text = "aaaaaaabaaaada"
        self.assertEquals(
            text,
            scramble.reverse_parse(scramble.parse(text, input), input))

    def test_revese_parse(self):
        input = [
            "swap position 4 with position 0",
            "swap letter d with letter b",
            "reverse positions 0 through 4",
            "rotate left 1 step",
            "move position 1 to position 4",
            "move position 3 to position 0",
            "rotate based on position of letter b",
            "rotate based on position of letter d",
            "rotate right 2 steps",
        ]

        self.assertEquals("abcde", scramble.reverse_parse("abdec", input))

    def test_actual_input2(self):
        lines = [line.strip() for line in open("input.txt")]
        self.assertEquals("egcdahbf",
                          scramble.reverse_parse("fbgdceah", lines))
