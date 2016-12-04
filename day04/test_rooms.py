import unittest
from rooms import *

class RoomTest(unittest.TestCase):
    def test_calculate_checksum(self):
        self.assertEquals("abxyz", calculate_checksum("aaaaa-bbb-z-y-x-123"))
        self.assertEquals("abcde", calculate_checksum("a-b-c-d-e-f-g-h-987"))
        self.assertEquals("oarel", calculate_checksum("not-a-real-room-404"))
        self.assertNotEquals("decoy", calculate_checksum("totally-real-room-200"))

    def test_compare(self):
        self.assertEquals(-1, cmp_by_number_then_alphabet(("b",5),("c",4)))
        self.assertEquals(1, cmp_by_number_then_alphabet(("b",5),("c",6)))
        self.assertEquals(-1, cmp_by_number_then_alphabet(("b",5),("c",5)))
        self.assertEquals(1, cmp_by_number_then_alphabet(("b",5),("a",5)))

    def test_check_multiple_checksums(self):
        f = ["aaaaa-bbb-z-y-x-123[abxyz]",
        "a-b-c-d-e-f-g-h-987[abcde]",
        "not-a-real-room-404[oarel]",
        "totally-real-room-200[decoy]"]

        self.assertEquals(1514, sum_from_lines(f))

