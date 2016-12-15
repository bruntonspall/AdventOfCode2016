import unittest
from hashcode import *

class RoomTest(unittest.TestCase):
    def test_simple_hash(self):
        self.assertEquals(valid_hash("abc3231928"), "")
        self.assertEquals(valid_hash("abc3231929"), "1")

    def test_find_hash(self):
        self.assertEquals(find_hash("abc", 0), ("1", 3231929))
        self.assertEquals(find_hash("abc", 3231930), ("8", 5017308))

    def test_8digitcode(self):
        self.assertEquals(find_code("abc"), "18f47a30")
