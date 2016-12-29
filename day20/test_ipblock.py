import unittest
import ipblock


class TestIPBlock(unittest.TestCase):
    def test_simple_block(self):
        block = ipblock.IPBlock()
        block.add_block("5-8")
        block.add_block("0-2")
        block.add_block("4-7")
        self.assertEquals(3, block.first_allowed())

    def test_large_block(self):
        block = ipblock.IPBlock()
        block.add_block("0-1847080")
        block.add_block("1847081-4852291")
        self.assertEquals(4852292, block.first_allowed())

    def test_actual_input(self):
        lines = [l.strip() for l in open("input.txt")]
        block = ipblock.IPBlock()
        for line in lines:
            block.add_block(line)
        self.assertEquals(14975795, block.first_allowed())

    def test_count_allowed_simple(self):
        block = ipblock.IPBlock()
        block.add_block("0-1847080")
        block.add_block("1847083-4294967295")
        self.assertEquals(2, block.count_allowed())

    def test_count_allowed_complex(self):
        block = ipblock.IPBlock()
        block.add_block("0-20")
        block.add_block("21-39")
        block.add_block("41-60")
        block.add_block("62-4294967295")
        self.assertEquals(2, block.count_allowed())

    def test_count_allowed_overlapping(self):
        block = ipblock.IPBlock()
        block.add_block("0-60")
        block.add_block("21-39")
        block.add_block("41-60")
        block.add_block("62-4294967295")
        self.assertEquals(1, block.count_allowed())

    def test_count_actual_input(self):
        lines = [l.strip() for l in open("input.txt")]
        block = ipblock.IPBlock()
        for line in lines:
            block.add_block(line)
        self.assertEquals(101, block.count_allowed())
