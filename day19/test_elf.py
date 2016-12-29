import unittest
import elf


class ElfTest(unittest.TestCase):
    def test_elf_rotate(self):
        self.assertEquals(3, elf.ll_solve_left(5))

    def test_elf_opposite(self):
        self.assertEquals(2, elf.ll_solve_opposite(5))
        self.assertEquals(6, elf.ll_solve_opposite(15))
        self.assertEquals(10, elf.ll_solve_opposite(50))

    # def test_actual_input(self):
    #     self.assertEquals(1815603, elf.ll_solve_left(3004953))

    # def test_actual_input2(self):
    #     self.assertEquals(1410630, elf.ll_solve_opposite(3004953))
