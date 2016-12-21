from bitarray import bitarray
import re
MASK = bitarray("00111111")


class Display(object):
    """docstring for Display."""
    def __init__(self):
        super(Display, self).__init__()
        self.col = []
        for x in range(50):
            self.col.append(bitarray("000000"))

    def rect(self, w, h):
        for x in range(w):
            self.col[x][0:h] = True

    def rotate_column(self, col, amount):
        val = self.col[col]
        for x in range(amount):
            val.insert(0, val.pop())
        self.col[col] = val

    def rotate_row(self, row, amount):
        for n in range(amount):
            new_row = [c[row] for c in self.col]
            new_row.insert(0, new_row.pop())
            for i, x in enumerate(self.col):
                self.col[i][row] = new_row[i]

    def render(self):
        output = []
        for row in range(6):
            output.append("")
            for x in range(50):
                if self.col[x][row]:
                    output[row] += "#"
                else:
                    output[row] += "."
        return output

    def parse(self, lines):
        for line in lines:
            m = re.match("rect (\d+)x(\d+)", line)
            if m:
                self.rect(int(m.group(1)), int(m.group(2)))
            m = re.match("rotate row y=(\d+) by (\d+)", line)
            if m:
                self.rotate_row(int(m.group(1)), int(m.group(2)))
            m = re.match("rotate column x=(\d+) by (\d+)", line)
            if m:
                self.rotate_column(int(m.group(1)), int(m.group(2)))

    def count_pixels(self):
        return sum([c.count() for c in self.col])


if __name__ == '__main__':
    f = open("input.txt")
    lines = [l.strip() for l in f.readlines()]
    d = Display()
    d.parse(lines)
    for l in d.render():
        print l
