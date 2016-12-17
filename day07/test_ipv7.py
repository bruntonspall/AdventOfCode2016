import unittest
from ipv7 import parse_address, is_palindrome, contains_abba, is_valid_addr


class TestIPv7(unittest.TestCase):
    def test_parseIPv7Address(self):
        self.assertEquals((["abba", "qrst"], ["mnop"]),
                          parse_address("abba[mnop]qrst"))

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("ABBA"))
        self.assertTrue(is_palindrome("abba"))
        self.assertTrue(is_palindrome("bddb"))
        self.assertTrue(is_palindrome("aaaa"))
        self.assertFalse(is_palindrome("abcd"))
        self.assertFalse(is_palindrome("jkla"))

    def test_contains_abba(self):
        self.assertTrue(contains_abba("abba[mnop]qrst"))
        self.assertTrue(contains_abba("abcd[bddb]xyyx"))
        self.assertFalse(contains_abba("aaaa[qwer]tyui"))
        self.assertTrue(contains_abba("ioxxoj[asdfgh]zxcvbn"))
        self.assertTrue(contains_abba("ioxxoj"))
        self.assertTrue(contains_abba("abba"))

    def test_is_valid_addr(self):
        self.assertTrue(is_valid_addr("abba[mnop]qrst"))
        self.assertFalse(is_valid_addr("abcd[bddb]xyyx"))
        self.assertFalse(is_valid_addr("aaaa[qwer]tyui"))
        self.assertTrue(is_valid_addr("ioxxoj[asdfgh]zxcvbn"))

    def test_is_valid_complex_addr(self):
        self.assertTrue(is_valid_addr("fgabbatw[mnop]qasdrst[uvwx]iuytre"))
        self.assertTrue(is_valid_addr("fgabcatw[mnop]qassast[uvwx]iuytre"))
        self.assertTrue(is_valid_addr("fgabcatw[mnop]qasdrst[uvwx]iabbae"))
        self.assertFalse(is_valid_addr("abcd[zxcv]bnmkjgfdfj[bddb]xyyx"))
        self.assertFalse(is_valid_addr("abcd[bddb]bnmkjgfdfj[zxcv]xyyx"))
