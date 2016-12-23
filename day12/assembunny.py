class CPU(object):
    def __init__(self):
        super(CPU, self).__init__()
        self.instructions = []
        self.registers = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.isHalted = False
        self.pc = 0

    def step(self):
        if self.isHalted:
            return
        opcode = self.instructions[self.pc][0]
        if opcode == 0:
            opcode, src, dest = self.instructions[self.pc]
            if src.isdigit():
                self.registers[dest] = int(src)
            else:
                self.registers[dest] = self.registers[src]
            self.pc += 1
        elif opcode == 1:
            opcode, reg = self.instructions[self.pc]
            self.registers[reg] += 1
            self.pc += 1
        elif opcode == 2:
            opcode, reg = self.instructions[self.pc]
            self.registers[reg] -= 1
            self.pc += 1
        elif opcode == 3:
            opcode, reg, jmp = self.instructions[self.pc]
            if not reg.isdigit() and self.registers[reg] != 0:
                self.pc += int(jmp)
            elif reg.isdigit() and int(reg) != 0:
                self.pc += int(jmp)
            else:
                self.pc += 1
        if self.pc >= len(self.instructions):
            self.isHalted = True

    def load(self, lines):
        LOOKUP = {
            "cpy": 0,
            "inc": 1,
            "dec": 2,
            "jnz": 3}
        for line in lines:
            opcode = LOOKUP[line[0:3]]
            op = line.split()
            op[0] = opcode
            self.instructions.append(op)

    def run(self):
        while not self.isHalted:
            self.step()

    def run_render(self):
        import time
        self.render()
        while not self.isHalted:
            self.step()
            self.render()
            time.sleep(0.5)

    def render(self):
        print "CPU running: ", self.isHalted, " PC: ", self.pc
        for reg, val in self.registers.items():
            print "Reg ", reg, ": ", val
        ops = [(i, op) for i, op in enumerate(self.instructions)
               if self.pc-5 < i < self.pc+5]
        for op in ops:
            if op[0] == self.pc:
                print "->", op[0], op[1]
            else:
                print "  ", op[0], op[1]


if __name__ == '__main__':
    f = open("input.txt")
    lines = [l.strip() for l in f]
    cpu = CPU()
    cpu.load(lines)
    cpu.run()
    cpu.render()
