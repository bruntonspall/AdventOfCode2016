import re

r = re.compile("(.*)\[(.*)\](.*)")


def parse_address(addr):
    addrs = []
    hypernets = []
    while addr:
        if addr[0] == "[":
            hypernets.append(addr[1:addr.find("]")])
            addr = addr[addr.find("]")+1:]
        if addr.find("[") == -1:
            addrs.append(addr)
            addr = ""
        else:
            addrs.append(addr[:addr.find("[")])
            addr = addr[addr.find("["):]

    return addrs, hypernets


def is_palindrome(word):
    return "".join(reversed(word)) == word


def is_abba(word):
    return (len(word) == 4) and \
           is_palindrome(word) and \
           word[0] != word[1]


def is_aba(word):
    return (len(word) == 3) and \
           is_palindrome(word) and \
           word[0] != word[1]


def contains_abba(word):
    word_in_fours = [word[n:n+4] for n in range(len(word)) if n+4 <= len(word)]
    for word in word_in_fours:
        if is_abba(word):
            return True
    return False


def is_valid_addr(addr):
    addrs, hypernets = parse_address(addr)
    if filter(contains_abba, hypernets):
        return False
    return len(filter(contains_abba, addrs)) > 0


def extract_aba(word):
    threes = [word[n:n+3] for n in range(len(word)) if n+3 <= len(word)]
    return filter(is_aba, threes)


def flatmap(fn, l):
    return reduce(list.__add__, map(fn, l))


def extract_aba_from_addr(addr):
    addrs, hypernets = parse_address(addr)
    return flatmap(extract_aba, addrs), flatmap(extract_aba, hypernets)


def convert_aba_to_bab(aba):
    return aba[1]+aba[0]+aba[1]


def supports_ssl(addr):
    aba_addrs, aba_hypernets = extract_aba_from_addr(addr)
    for aba in aba_hypernets:
        bab = convert_aba_to_bab(aba)
        if bab in aba_addrs:
            return True
    return False


if __name__ == "__main__":
    f = file("input.txt")
    lines = [l.strip() for l in f.readlines()]
    print len([l for l in lines if supports_ssl(l)])
