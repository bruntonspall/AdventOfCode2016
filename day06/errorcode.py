from collections import Counter


def rotate(l):
    return ["".join(x) for x in zip(*l)]


def most_frequent(word):
    return Counter(word).most_common(1)[0][0]


def least_frequent(word):
    return Counter(word).most_common()[-1][0]


def find_freq(l):
    return "".join([most_frequent(x) for x in rotate(l)])


def find_least_freq(l):
    return "".join([least_frequent(x) for x in rotate(l)])
