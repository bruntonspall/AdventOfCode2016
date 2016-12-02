import unittest
from doorcode import *

class DoorCodeTest(unittest.TestCase):
    def test_simple_doorcode(self):
        self.assertEquals(1, calculate_doorcode("ULL"))
        self.assertEquals(1, calculate_doorcode("UL"))
        self.assertEquals(1, calculate_doorcode("LUL"))
        self.assertEquals(2, calculate_doorcode("U"))
        self.assertEquals(2, calculate_doorcode("UU"))
        self.assertEquals(3, calculate_doorcode("UR"))
        self.assertEquals(3, calculate_doorcode("UUR"))
        self.assertEquals(3, calculate_doorcode("URR"))
        self.assertEquals(4, calculate_doorcode("L"))
        self.assertEquals(4, calculate_doorcode("LLL"))
        self.assertEquals(6, calculate_doorcode("R"))
        self.assertEquals(6, calculate_doorcode("RRR"))
        self.assertEquals(7, calculate_doorcode("DL"))
        self.assertEquals(7, calculate_doorcode("LD"))
        self.assertEquals(7, calculate_doorcode("LDLD"))
        self.assertEquals(8, calculate_doorcode("D"))
        self.assertEquals(8, calculate_doorcode("DD"))
        self.assertEquals(9, calculate_doorcode("DR"))
        self.assertEquals(9, calculate_doorcode("RD"))
        self.assertEquals(9, calculate_doorcode("DDR"))

    def test_complicated_doorcodes(self):
        self.assertEquals(1, calculate_doorcode("RRLLDDDUU"))
        self.assertEquals(2, calculate_doorcode("DDDUU"))
        self.assertEquals(3, calculate_doorcode("LLUDDUURLRRU"))
        self.assertEquals(4, calculate_doorcode("UUDLRRRLL"))
        self.assertEquals(5, calculate_doorcode("UDLRLRUD"))
        self.assertEquals(6, calculate_doorcode("RRRLUUDR"))
        self.assertEquals(7, calculate_doorcode("DLLRLUDL"))
        self.assertEquals(8, calculate_doorcode("URRRLDDDUDRL"))
        self.assertEquals(9, calculate_doorcode("UDDDUDRRLRUD"))

    def test_following_doorcode(self):
        self.assertEquals(1, calculate_doorcode("ULL"))
        self.assertEquals(9, calculate_doorcode("RRDDD", 1))
        self.assertEquals(8, calculate_doorcode("LURDL", 9))
        self.assertEquals(5, calculate_doorcode("UUUUD", 8))

    def test_rotated_simple_doorcode(self):
        self.assertEquals("3", calculate_rotated_doorcode("U","7"))
        self.assertEquals("B", calculate_rotated_doorcode("D","7"))
        self.assertEquals("6", calculate_rotated_doorcode("L","7"))
        self.assertEquals("8", calculate_rotated_doorcode("R","7"))

        self.assertEquals("2", calculate_rotated_doorcode("U","2"))
        self.assertEquals("6", calculate_rotated_doorcode("D","2"))
        self.assertEquals("2", calculate_rotated_doorcode("L","2"))
        self.assertEquals("3", calculate_rotated_doorcode("R","2"))

        self.assertEquals("1", calculate_rotated_doorcode("U","1"))
    def test_rotated_following_doorcode(self):
        self.assertEquals("5", calculate_rotated_doorcode("ULL", "5"))
        self.assertEquals("D", calculate_rotated_doorcode("RRDDD", "5"))
        self.assertEquals("B", calculate_rotated_doorcode("LURDL", "D"))
        self.assertEquals("3", calculate_rotated_doorcode("UUUUD", "B"))

