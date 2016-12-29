class IPBlock(object):
    def __init__(self):
        super(IPBlock, self).__init__()
        self.blocks = []

    def add_block(self, block):
        a, b = sorted(map(int, block.split("-")))
        self.blocks.append((a, b))

    def first_allowed(self):
        i = 0
        for x in sorted(self.blocks):
            if x[0] > i:
                return i
            else:
                i = max(i, x[1]+1)
        return i

    def count_allowed(self):
        count = 0
        i = 0
        for x in sorted(self.blocks):
            if x[0] > i:
                count += (x[0]-i)
            i = max(i, x[1]+1)
        return count
