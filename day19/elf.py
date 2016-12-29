def make_circle(min, max):
    elves = {}
    for x in range(min, max+1):
        elves[x] = 1
    return elves


def opposite(circle, elf):
    index = circle.keys().index(elf)
    new_index = index + len(circle)/2
    if new_index >= len(circle):
        return circle.keys()[new_index - len(circle)]
    else:
        return circle.keys()[new_index]


def left(circle, elf):
    index = circle.keys().index(elf)+1
    if index == len(circle):
        return circle.keys()[0]
    else:
        return circle.keys()[index]


def circle(numberOfElves, fn=left):
    elves = make_circle(1, numberOfElves)
    while len(elves) > 1:
        for x in elves.keys():
            if x in elves:
                nextElf = fn(elves, x)
                # elves[x] += elves[nextElf]
                del elves[nextElf]
    return elves.items()[0][0]


# The solutions above were incredibly slow and the mid seems to be wrong
# A hint online pointed out that using a linked list, and moving the midpoint
# forwards by 2 every other deletion is much more efficient


class Node(object):
    """A simple linked list implementation"""
    def __init__(self, id):
        super(Node, self).__init__()
        self.id = id
        self.next = None
        self.prev = None

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev


def ll_make_circle(min, max):
    l = [Node(i) for i in range(min, max+1)]
    for n in range(max):
        l[n].next = l[(n+1) % (max)]
        l[n].prev = l[(n-1) % (max)]
    return l[0]


def ll_print_circle(start):
    node = start
    print node.id
    node = node.next
    while node.id != start.id:
        print node.id
        node = node.next


def ll_solve_left(numberOfElves):
    circle = ll_make_circle(1, numberOfElves)
    elf = circle
    for x in xrange(numberOfElves-1):
        # print elf.id, " stealing from ", elf.next.id
        elf.next.delete()
        elf = elf.next
    return elf.id


def ll_solve_opposite(numberOfElves):
    circle = ll_make_circle(1, numberOfElves)
    elf = circle
    mid = circle
    for x in xrange(numberOfElves/2):
        mid = mid.next
    for x in xrange(numberOfElves-1):
        # print elf.id, " stealing from ", mid.id, x

        mid.delete()
        mid = mid.next
        if x % 2 == 0:
            mid = mid.next
        elf = elf.next
    return elf.id
