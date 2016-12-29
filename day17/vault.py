import hashlib
import heapq


DIRECTIONS = "UDLR"


def _open(char):
    return char in "bcdef"


def get_doors(input):
    hash = hashlib.md5(input).hexdigest()
    return [_open(h) for h in hash[0:4]]


def get_location(path):
    return path.count("R") - path.count("L"), path.count("D") - path.count("U")


def valid_direction((x, y)):
    return [y > 0, y < 3, x > 0, x < 3]


def find_path(input):
    openlist = []
    heapq.heappush(openlist, (len(input), input))
    while openlist:
        print "Open: ", openlist
        x, node = heapq.heappop(openlist)
        doors = get_doors(node)
        directions = valid_direction(get_location(node))
        d = [DIRECTIONS[i] for i, v in enumerate(doors) if v and directions[i]]
        print "Node: ", node, doors, directions, d
        for dir in d:
            print node, dir
            heapq.heappush(openlist, (len(node+dir), node+dir))
            if get_location(node+dir) == (3, 3):
                return (node+dir)[len(input):]
    return None


def find_longest_path(input):
    openlist = []
    openlist.append(input)
    longest_path = ""
    while len(openlist) > 0:
        node = openlist.pop()
        doors = get_doors(node)
        directions = valid_direction(get_location(node))
        d = [DIRECTIONS[i] for i, v in enumerate(doors) if v and directions[i]]
        for dir in d:
            path = node+dir
            if get_location(path) == (3, 3):
                if len(path) > len(longest_path):
                    longest_path = path
            else:
                if path not in openlist:
                    openlist.append(path)
    return longest_path[len(input):]
