LOOKUP = {
    "...": ".",
    "^..": "^",
    ".^.": ".",
    "..^": "^",
    "^^.": "^",
    ".^^": "^",
    "^.^": ".",
    "^^^": ".",
}


def get_three_from_line(x, line):
    if x == 0:
        return "."+line[0:2]
    if x == len(line)-1:
        return line[-2:]+"."
    return line[x-1:x+2]


def next_line(line):
    return "".join(
        [LOOKUP[get_three_from_line(i, line)] for i, c in enumerate(line)])


def make_grid(line, l):
    grid = [line]
    while len(grid) < l:
        grid.append(next_line(grid[-1]))
    return grid


def count_safe(line, count):
    csum = 0
    while True:
        if count == 0:
            return csum
        csum += line.count(".")
        line = next_line(line)
        count -= 1
