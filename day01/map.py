def readDirections(directionsString):
    return directionsString.split(", ")

def nextDirection(start, heading, direction):
    if direction[0] == "R":
        distance = int(direction[1:])
        heading = (heading +1) % 4
    elif direction[0] == "L":
        distance = int(direction[1:])
        heading = (heading -1) % 4

    if heading == 0:
        return [start[0],start[1] + distance],heading
    elif heading == 1:
        return [start[0]+distance,start[1]],heading
    elif heading == 2:
        return [start[0],start[1] - distance],heading
    elif heading == 3:
        return [start[0]-distance,start[1]],heading

def expandDirections(start, heading, direction):
    end, heading = nextDirection(start, heading, direction)
    l = []
    if heading == 0:
        for y in range(start[1],end[1]):
            l.append([end[0], y])
    if heading == 1:
        for x in range(start[0],end[0]):
            l.append([x,end[1]])
    if heading == 2:
        for y in range(start[1],end[1], -1):
            l.append([end[0], y])
    if heading == 3:
        for x in range(start[0],end[0], -1):
            l.append([x,end[1]])
    return l

def followDirections(directions):
    heading = 0
    distance = 0
    coords = [0,0]
    for direction in directions:
        coords, heading = nextDirection(coords, heading, direction)
    return coords

def followDirections2(directions):
    heading = 0
    distance = 0
    coords = [0,0]
    visited = []
    for direction in directions:
        vis = expandDirections(coords, heading, direction)
        for v in vis:
            if v in visited:
                return v
            visited.append(v)
        coords, heading = nextDirection(coords, heading, direction)
    return coords

def calculateDistance(coord):
    return abs(coord[0]) + abs(coord[1])

import pdb

directionsString = open("directions.txt").readlines()[0].strip()
directions = readDirections(directionsString)
print directions
end = followDirections2(directions)
print end
print calculateDistance(end)
