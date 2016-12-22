import re
from collections import defaultdict


class Bot(object):
    def __init__(self, name="", hi=None, lo=None):
        super(Bot, self).__init__()
        self.name = name
        self.hi = hi
        self.lo = lo
        self.compared = []

    def giveValue(self, v):
        self.compared.append(v)
        if len(self.compared) > 1:
            self.hi.giveValue(max(self.compared))
            self.lo.giveValue(min(self.compared))


class Output(object):
    def __init__(self, name=""):
        super(Output, self).__init__()
        self.name = name
        self.bin = []

    def giveValue(self, v):
        self.bin.append(v)


def parse(lines):
    bots, outputs = defaultdict(Bot), defaultdict(Output)
    for line in sorted(lines):
        m = re.match("value (\d+) goes to bot (\d+)", line)
        if m:
            bot = bots[int(m.group(2))]
            value = int(m.group(1))
            bot.giveValue(value)
        m = re.match("bot (\d+) gives low to (bot|output) (\d+) and "
                     "high to (bot|output) (\d+)", line)
        if m:
            bot = bots[int(m.group(1))]
            bot.name = "Bot "+m.group(1)
            lo, hi = None, None
            if m.group(2) == "bot":
                lo = bots[int(m.group(3))]
                lo.name = "Bot "+m.group(3)
            else:
                lo = outputs[int(m.group(3))]
                lo.name = "Ouput "+m.group(3)
            if m.group(4) == "bot":
                hi = bots[int(m.group(5))]
                hi.name = "Bot "+m.group(5)
            else:
                hi = outputs[int(m.group(5))]
                hi.name = "Output "+m.group(5)
            bot.lo = lo
            bot.hi = hi
    return bots, outputs


if __name__ == '__main__':
    f = open("input.txt")
    lines = [l.strip() for l in f.readlines()]
    bots, outputs = parse(lines)
    for bot in bots.values():
        if sorted(bot.compared) == [17, 61]:
            print bot.name
    print outputs[0].bin
    print outputs[1].bin
    print outputs[2].bin
