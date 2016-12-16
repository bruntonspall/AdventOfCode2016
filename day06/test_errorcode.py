import unittest
from errorcode import *


class ErrorCodeTest(unittest.TestCase):
    def test_lengthwise_rotate(self):
        input = ["abc", "def", "ghi"]
        self.assertEquals(rotate(input), ["adg", "beh", "cfi"])

    def test_most_frequent(self):
        self.assertEquals(most_frequent("aaabbccd"), "a")
        self.assertEquals(most_frequent("aabbbbccd"), "b")

    def test_find_freq(self):
        input = ["eedadn", "drvtee", "eandsr", "raavrd", "atevrs", "tsrnev",
                 "sdttsa", "rasrtv", "nssdts", "ntnada", "svetve", "tesnvt",
                 "vntsnd", "vrdear", "dvrsen", "enarar"]
        self.assertEquals(find_freq(input), "easter")
