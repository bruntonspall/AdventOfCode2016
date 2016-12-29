import unittest
import vault


class VaultTest(unittest.TestCase):
    def test_get_doors(self):
        self.assertEquals([1, 1, 1, 0],
                          vault.get_doors("hijkl"))

    def test_get_location(self):
        self.assertEquals((2, 1), vault.get_location("DURRD"))
        self.assertEquals((3, 3), vault.get_location("DDUDRLRRUDRD"))
        self.assertEquals((3, 3),
                          vault.get_location("DRURDRUDDLLDLUURRDULRLDUUDDDRR"))

    def test_is_valid_direction(self):
        self.assertEquals([0, 1, 0, 1], vault.valid_direction((0, 0)))
        self.assertEquals([0, 1, 1, 1], vault.valid_direction((1, 0)))
        self.assertEquals([0, 1, 1, 0], vault.valid_direction((3, 0)))
        self.assertEquals([1, 1, 1, 1], vault.valid_direction((1, 1)))

    def test_find_path(self):
        self.assertEquals("DDRRRD", vault.find_path("ihgpwlah"))
        self.assertEquals("DDUDRLRRUDRD", vault.find_path("kglvqrro"))
        self.assertEquals("DRURDRUDDLLDLUURRDULRLDUUDDDRR",
                          vault.find_path("ulqzkmiv"))

    def test_actual_input(self):
        self.assertEquals("DDRRULRDRD", vault.find_path("veumntbg"))

    def test_find_longest_path(self):
        self.assertEquals(370, len(vault.find_longest_path("ihgpwlah")))

    def test_find_actual_longest_path(self):
        self.assertEquals(536, len(vault.find_longest_path("veumntbg")))
