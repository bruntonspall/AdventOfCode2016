import unittest
import traps


class TrapsTest(unittest.TestCase):
    def test_next_line(self):
        self.assertEquals(".^^^^", traps.next_line("..^^."))
        self.assertEquals("^^..^", traps.next_line(".^^^^"))
        self.assertEquals("^^^...^..^", traps.next_line(".^^.^.^^^^"))

    def test_get_three(self):
        self.assertEquals("..^", traps.get_three_from_line(0, ".^^."))
        self.assertEquals(".^^", traps.get_three_from_line(1, ".^^."))
        self.assertEquals("^^.", traps.get_three_from_line(2, ".^^."))
        self.assertEquals("^..", traps.get_three_from_line(3, ".^^."))

    def test_count_in_grid(self):
        self.assertEquals(7, traps.count_safe(".^^^^", 5))
        self.assertEquals(38, traps.count_safe(".^^.^.^^^^", 10))

    def test_make_grid(self):
        self.assertEquals([
            ".^^^^",
            "^^..^",
            "^^^^.",
            "^..^^",
            ".^^^^"
        ], traps.make_grid(".^^^^", 5))

    def test_actual_count(self):
        s = ".^^^^^.^^.^^^.^...^..^^.^.^.." \
            "^^^^^^^^^^..^...^^.^..^^^^..^" \
            "^^^...^.^.^^^^^^^^....^..^^^^" \
            "^^.^^^.^^^.^^"
        self.assertEquals(1989, traps.count_safe(s, 40))

    def test_part_2_count(self):
        s = ".^^^^^.^^.^^^.^...^..^^.^.^.." \
            "^^^^^^^^^^..^...^^.^..^^^^..^" \
            "^^^...^.^.^^^^^^^^....^..^^^^" \
            "^^.^^^.^^^.^^"
        self.assertEquals(19999894, traps.count_safe(s, 400000))
