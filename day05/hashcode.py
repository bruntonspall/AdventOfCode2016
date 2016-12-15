import hashlib

def valid_hash(code):
    h = hashlib.md5(code).hexdigest()
    if h[0:5] == "00000":
        return h[5]
    else:
        return ""

def find_hash(code, start):
    found = False
    h = ""
    while not found:
        h = valid_hash(code+str(start))
        if h:
            found = True
        else:
            start += 1
    return h, start

def find_code(code):
    password = ""
    start = 0
    while len(password) < 8:
        h, start = find_hash(code, start)
        password += h
        start += 1
    return password
