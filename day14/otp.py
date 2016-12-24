import hashlib
import re

TRIPLE = re.compile(r"([0-9a-f])\1\1")
FIVE = re.compile(r"([0-9a-f])\1\1\1\1")


def hash(salt, num):
    s = hashlib.md5(salt+str(num)).hexdigest()
    for x in range(2016):
        s = hashlib.md5(s).hexdigest()
    return s


def has_triple(salt, num):
    return TRIPLE.search(hash(salt, num))


def has_five(salt, num):
    return FIVE.search(hash(salt, num))


def gen_precalc(salt):
    fives = {}
    triples = {}
    for x in range(25000):
        m = has_five(salt, x)
        if m:
            fives[x] = m.group(1)
        m = has_triple(salt, x)
        if m:
            triples[x] = m.group(1)
    return fives, triples


def is_valid(num, fives, triples):
    if num in triples:
        options = [k for k in fives.keys() if num < k < num+1000]
        for tr in options:
            if fives[tr] == triples[num]:
                return tr, num
    return False, False


if __name__ == '__main__':
    f, t = gen_precalc("zpqevtbw")
    x = 0
    find = []
    while len(find) < 64:
        x += 1
        tr, num = is_valid(x, f, t)
        if tr:
            print x, num, t[num], tr, f[tr]
            find.append(x)
