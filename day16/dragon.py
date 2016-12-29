import string
T = string.maketrans("01", "10")


def _expand(data):
    return data+"0"+"".join(reversed(data.translate(T)))


def expand(length, data):
    while len(data) < length:
        data = _expand(data)
    return data[0:length]


CHECKSUMS = {
    ("0", "0"): "1",
    ("0", "1"): "0",
    ("1", "0"): "0",
    ("1", "1"): "1"
}


def checksum(data):
    data = [CHECKSUMS[a] for a in zip(data[::2], data[1::2])]
    if (len(data) % 2) == 1:
        return "".join(data)
    else:
        return checksum(data)
