import unittest
from triangles import validate

class TriangleTest(unittest.TestCase):
    def test_validate_triangle(self):
        self.assertFalse(validate(5,10,25))
        self.assertFalse(validate(5,25,10))
        self.assertFalse(validate(10,25,5))

    def test_validate_set(self):
        self.assertTrue(validate(541,588,421))
        self.assertFalse(validate(827,272,126))
        self.assertTrue(validate(660,514,367))
