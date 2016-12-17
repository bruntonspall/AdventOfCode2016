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
