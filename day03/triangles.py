def validate(n1,n2,n3):
    a,b,c = sorted([n1,n2,n3])
    return a+b>c

def parse(filename):
    lines = open(filename).readlines()
    count = 0
    for line in lines:
        a,b,c = [int(x) for x in line.split()]
        if validate(a,b,c):
            count += 1
    return count

def parse2(filename):
    lines = open(filename).readlines()
    count = 0
    for i in range(len(lines)/3):
        offset = 3*i
        line1 = [int(x) for x in lines[offset].split()]
        line2 = [int(x) for x in lines[offset+1].split()]
        line3 = [int(x) for x in lines[offset+2].split()]
        if validate(line1[0], line2[0], line3[0]):
            count += 1
        if validate(line1[1], line2[1], line3[1]):
            count += 1
        if validate(line1[2], line2[2], line3[2]):
            count += 1
    return count
