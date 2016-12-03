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
