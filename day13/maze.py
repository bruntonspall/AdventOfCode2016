import heapq


def bits(num):
    count = 0
    while num > 0:
        if num & 1:
            count += 1
        num >>= 1
    return count % 2


class Location(object):
    def __init__(self, coords, fScore, gScore):
        self.coords = coords
        self.fScore = fScore
        self.gScore = gScore

    def __eq__(self, other):
        return self.coords == other.coords

    def __hash__(self):
        return hash(self.coords)

    def __lt__(self, other):
        return self.fScore < other.fScore

    def __repr__(self):
        return "({},{},{},{})".format(self.coords[0],
                                      self.coords[1],
                                      self.fScore,
                                      self.gScore)


class Maze(object):
    """docstring for Maze."""
    def __init__(self, init):
        super(Maze, self).__init__()
        self.init = init

    def get(self, coord):
        x, y = coord
        return bits((x*x)+(3*x)+(2*x*y)+y+(y*y)+self.init)

    def find_route(self, start, end):
        def h(c, dst):
            return abs(c[0]-dst[0])+abs(c[1]-dst[1])

        def passable(n):
            if n[0] < 0 or n[1] < 0:
                return 1000
            return (self.get(n) * 1000) + 1

        sx, sy = start
        dx, dy = end
        startL = Location(start, 0, h(start, end))
        openlist = []
        heapq.heappush(openlist, startL)
        closedlist = []
        locations = {start: startL}
        fromPath = {
        }

        while len(openlist) > 0:
            # print "### DEBUG ###"
            # print "Open:    ", openlist
            # print "Closed:  ", closedlist
            # print "Frompath:", fromPath

            current = heapq.heappop(openlist)
            if current.coords == end:
                current = current.coords
                path = [current]
                while current in fromPath.keys():
                    current = fromPath[current]
                    path.append(current)
                path.reverse()
                return path
            closedlist.insert(0, current.coords)
            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbour = (current.coords[0]+d[0], current.coords[1]+d[1])
                if neighbour in closedlist:
                    continue
                score = locations[current.coords].gScore + passable(neighbour)
                n = Location(neighbour, score, score+h(neighbour, end))
                if neighbour not in locations:
                    locations[neighbour] = n
                if n not in openlist:
                    heapq.heappush(openlist, n)
                elif score >= locations[neighbour].gScore:
                    continue
                fromPath[neighbour] = current.coords

    def nearby(self, start, distance):
        openlist = [start]
        closedlist = []
        distances = {start: 0}
        while len(openlist) > 0:
            # print "### DEBUG ###"
            # print "OpenList   :", openlist
            # print "ClosedList :", closedlist
            # print "Distances  :", distances
            current = openlist.pop()
            closedlist.append(current)
            curdist = distances[current]
            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                n = current[0]+d[0], current[1]+d[1]
                if n in closedlist:
                    continue
                if n in openlist:
                    continue
                if n[0] >= 0 and n[1] >= 0 and self.get(n) == 0:
                    if n not in distances:
                        distances[n] = curdist+1
                    elif distances[n] > curdist+1:
                        distances[n] = curdist + 1
                    if distances[n] <= distance:
                        openlist.append(n)
        return closedlist

    def render(self, w=10, h=10, hilight=None):
        if not hilight:
            hilight = []
        for y in range(h):
            line = ""
            for x in range(w):
                if (x, y) in hilight:
                    line += "*"
                elif self.get((x, y)):
                    line += "#"
                else:
                    line += "."
            print line
