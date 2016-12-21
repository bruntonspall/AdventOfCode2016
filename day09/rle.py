def decode(i):
    state = 0
    out = ""
    buf = ""
    charnum = 0
    repeatcount = 0
    for letter in i:
        if state == 0:
            if letter == "(":
                state = 1
            else:
                out += letter
        elif state == 1:
            if letter == "x":
                state = 2
                charnum = int(buf)
                buf = ""
            else:
                buf += letter
        elif state == 2:
            if letter == ")":
                state = 3
                repeatcount = int(buf)
                buf = ""
            else:
                buf += letter
        elif state == 3:
            buf += letter
            charnum -= 1
            if charnum == 0:
                out += (buf * repeatcount)
                buf = ""
                state = 0
        print "state: {} charnum: {} repeatcount: {} "\
              "buf: {}".format(state, charnum, repeatcount, buf)

    return out


def decode_length(i):
    state = 0
    out = 0
    buf = ""
    charnum = 0
    repeatcount = 0
    for letter in i:
        if state == 0:
            if letter == "(":
                state = 1
            else:
                out += 1
        elif state == 1:
            if letter == "x":
                state = 2
                charnum = int(buf)
                buf = ""
            else:
                buf += letter
        elif state == 2:
            if letter == ")":
                state = 3
                repeatcount = int(buf)
                buf = ""
            else:
                buf += letter
        elif state == 3:
            buf += letter
            charnum -= 1
            if charnum == 0:
                out += (decode_length(buf) * repeatcount)
                buf = ""
                state = 0
    return out


if __name__ == '__main__':
    f = file("input.txt")
    lines = [l.strip() for l in f.readlines()]
    ans = decode_length(lines[0])
    print ans
