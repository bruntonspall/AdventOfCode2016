import hashlib

def valid_hash(code):
    h = hashlib.md5(code).hexdigest()
    if h[0:5] == "00000":
        return h[5],h[6]
    else:
        return "",""

def find_hash(code, start):
    found = False
    h = ""
    while not found:
        h,h2 = valid_hash(code+str(start))
        if h:
            found = True
        else:
            start += 1
    return h, start, h2

def find_code(code):
    password = ""
    start = 0
    while len(password) < 8:
        h, start, h2 = find_hash(code, start)
        password += h
        start += 1
    return password

def find_code2(code):
    password = [" "," "," "," "," "," "," "," "]
    start = 0
    while " " in password:
        h, start, h2 = find_hash(code, start)
        if h.isdigit() and int(h) < 8:
            if password[int(h)] == " ":
                password[int(h)] = h2
        start += 1
    return password
