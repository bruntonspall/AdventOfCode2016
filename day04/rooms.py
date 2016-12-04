def cmp_by_number_then_alphabet(x,y):
    if x[1] == y[1]:
        return cmp(x[0],y[0])
    else:
        return cmp(y[1], x[1])

def calculate_checksum(s):
    s = sorted(s.replace("-","")[:-3])
    d = {}
    for character in s:
        if character in d:
            d[character] += 1
        else:
            d[character] = 1
    return "".join([letter for letter,number in sorted(d.items(),cmp=cmp_by_number_then_alphabet)][0:5])

def sum_from_lines(f):
    total = 0
    for line in f:
        room = line[:-7]
        checksum = line[-6:-1]
        if calculate_checksum(room) == checksum:
            total += int(room[-3:])
        else:
            pass
    return total

