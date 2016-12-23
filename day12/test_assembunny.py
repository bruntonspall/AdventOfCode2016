import unittest
import assembunny


class AssemBunnyTest(unittest.TestCase):
    def test_copy_instruction(self):
        cpu = assembunny.CPU()
        cpu.instructions = [(0, "7", "a")]
        self.assertEquals(0, cpu.registers["a"])
        cpu.step()
        self.assertEquals(7, cpu.registers["a"])

    def test_copy_register(self):
        cpu = assembunny.CPU()
        cpu.instructions = [(0, "7", "a"), (0, "a", "b")]
        self.assertEquals(0, cpu.registers["a"])
        self.assertEquals(0, cpu.registers["b"])
        cpu.step()
        self.assertEquals(7, cpu.registers["a"])
        self.assertEquals(0, cpu.registers["b"])
        cpu.step()
        self.assertEquals(7, cpu.registers["a"])
        self.assertEquals(7, cpu.registers["b"])

    def test_inc(self):
        cpu = assembunny.CPU()
        cpu.instructions = [(1, "a")]
        cpu.registers["a"] = 7
        self.assertEquals(7, cpu.registers["a"])
        cpu.step()
        self.assertEquals(8, cpu.registers["a"])

    def test_dec(self):
        cpu = assembunny.CPU()
        cpu.instructions = [(2, "a")]
        cpu.registers["a"] = 7
        self.assertEquals(7, cpu.registers["a"])
        cpu.step()
        self.assertEquals(6, cpu.registers["a"])

    def test_jnz(self):
        cpu = assembunny.CPU()
        cpu.instructions = [(2, "a"), (3, "a", -1)]
        cpu.registers["a"] = 2
        self.assertEquals(2, cpu.registers["a"])
        self.assertEquals(0, cpu.pc)
        cpu.step()
        self.assertEquals(1, cpu.registers["a"])
        self.assertEquals(1, cpu.pc)
        cpu.step()
        self.assertEquals(1, cpu.registers["a"])
        self.assertEquals(0, cpu.pc)
        cpu.step()
        self.assertEquals(0, cpu.registers["a"])
        self.assertEquals(1, cpu.pc)
        cpu.step()
        self.assertEquals(2, cpu.pc)

    def test_parse(self):
        cpu = assembunny.CPU()
        cpu.load([
            "inc a",
            "dec b",
            "jnz a -1",
            "cpy 1 a",
            "cpy a b"
        ])
        self.assertEquals([
            [1, "a"],
            [2, "b"],
            [3, "a", "-1"],
            [0, "1", "a"],
            [0, "a", "b"]
        ], cpu.instructions)

    def test_multiple_program(self):
        """ Multiply 5x4 into register c """
        cpu = assembunny.CPU()
        cpu.load([
            "cpy 5 b",
            "cpy 4 a",
            "inc c",
            "dec a",
            "jnz a -2",
            "dec b",
            "jnz b -5"
        ])
        self.assertEquals(0, cpu.registers["a"])
        self.assertEquals(0, cpu.registers["b"])
        self.assertEquals(0, cpu.registers["c"])
        self.assertEquals(0, cpu.registers["d"])
        cpu.run()
        self.assertEquals(20, cpu.registers["c"])

    def test_odd_jnz(self):
        """ This is a weird construction, jnz 1 2
        It means always jump forwards two"""
        cpu = assembunny.CPU()
        cpu.load([
            "inc a",
            "jnz 1 -1"])
        cpu.step()
        cpu.step()
        self.assertEquals(0, cpu.pc)
