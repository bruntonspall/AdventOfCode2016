import unittest
import otp


class OTPTest(unittest.TestCase):
    def test_has_triple(self):
        self.assertTrue(otp.has_triple("abc", 18))
        self.assertFalse(otp.has_triple("abc", 19))

    def test_has_five(self):
        self.assertFalse(otp.has_five("abc", 19))
        self.assertTrue(otp.has_five("abc", 816))
