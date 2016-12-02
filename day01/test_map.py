import unittest
from map import *

class MapTest(unittest.TestCase):
    def test_readDirections(self):
        directions = readDirections("L5, R6")
        self.assertEquals(directions, ["L5", "R6"])

    def test_followSimpleDirection(self):
        coords = followDirections(["R2"])
        self.assertEquals(coords, [2,0])

        coords = followDirections(["L2"])
        self.assertEquals(coords, [-2,0])

    def test_followMultistepDirection(self):
        coords = followDirections(["R2", "L1"])
        self.assertEquals(coords, [2,1])

        coords = followDirections(["R5", "L5", "R5", "R3"])
        self.assertEquals(coords, [10,2])

    def test_calculateDistance(self):
        self.assertEquals(calculateDistance([10,2]), 12)
        self.assertEquals(calculateDistance([10,-2]), 12)

    def test_basicTestCases(self):
        self.assertEquals(5, calculateDistance(followDirections(readDirections("R2, L3"))))
        self.assertEquals(2, calculateDistance(followDirections(readDirections("R2, R2, R2"))))
        self.assertEquals(12, calculateDistance(followDirections(readDirections("R5, L5, R5, R3"))))

    def test_expandWalk(self):
        self.assertEquals([[0,0],[1,0],[2,0],[3,0]], expandDirections([0,0], 0, "R4"))
        self.assertEquals([[4,0],[4,-1],[4,-2],[4,-3]], expandDirections([4,0], 1, "R4"))

    def test_followDirections2(self):
        self.assertEquals([4,0], followDirections2(["R8", "R4", "R4", "R8"]))
