from collections import Counter

def cmp_by_number_then_alphabet(x,y):
    if x[1] == y[1]:
        return cmp(x[0],y[0])
    else:
        return cmp(y[1], x[1])

def calculate_checksum(s):
    c = Counter(s.replace("-","")[:-3])
    counts = sorted(c.most_common(), cmp=cmp_by_number_then_alphabet)[:5]
    return "".join([letter for letter,number in counts])

def sum_from_lines(f):
    total = 0
    for line in f:
        room = line[:-7]
        if calculate_checksum(room) == line[-6:-1]:
            total += int(room[-3:])
    return total

