from collections import deque
import sys
input = sys.stdin.readline

# Note: Top, Bottom, Right, Left boundaries are added to the map
# That means +2 for h and w values!

dyx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def findPrisoner(h, w, jail):
    plist = []
    for y in range(h+2):
        for x in range(w+2):
            if jail[y][x] == '$':
                plist.append([y, x])
    return plist

# bfs-travels through the grid, and creates a "route" of path cost
# that increases for each door encountered
def route(h, w, start, jail):
    visited = [[-1]*(w+2) for _ in range(h+2)]
    visited[start[0]][start[1]] = 0
    q = deque()
    q.append(start)

    while q:
        cy, cx = q.popleft()
        for dy, dx in dyx:
            ny, nx = cy+dy, cx+dx
            if 0 <= ny < h+2 and 0 <= nx < w+2 and visited[ny][nx] < 0:
                if jail[ny][nx] == '*':
                    continue

                if jail[ny][nx] == '#':
                    visited[ny][nx] = visited[cy][cx]+1
                    q.append((ny, nx))
                else:
                    visited[ny][nx] = visited[cy][cx]
                    q.appendleft((ny, nx))

    return visited

def jailbreak(h, w, jail):
    startpoints = findPrisoner(h, w, jail)
    startpoints.append([0, 0])              # adding boundary location
    routes = {}

    for startpoint in startpoints:
        # r is a dictionary of startpoint: route!
        r = route(h, w, startpoint, jail)
        routes[tuple(startpoint)] = r

    minDoors = float('inf')
    for y in range(h+2):
        for x in range(w+2):
            # check if a cell is visit-able for all 3 bfs traversals
            # redundant, but:
            # need to check if a cell is visited by bfs anyways, so leave it
            allVisited = all(r[y][x] != -1 for _, r in routes.items())
            if allVisited:
                # sum the cost of reaching that cell!
                totalDoors = sum(r[y][x] for _, r in routes.items())
                # if it is a door cell, it's value has been +1'd for all three bfs'.
                # account for that; subtract 2.
                if jail[y][x] == '#':
                    totalDoors -= 2
                # update minimal door cost
                minDoors = min(minDoors, totalDoors)

    return minDoors

def printGrid(grid):
    for i in range(len(grid)):
        print(''.join(grid[i]))
    print()

def printRoute(route):
    for i in range(h+2):
        for j in range(w+2):
            if route[i][j] < 0:
                print('_', end="")
            else:
                print(str(route[i][j]), end="")
        print()
    print()


if __name__ == "__main__":
    testcase = int(input().strip())
    solutions = []

    for i in range(testcase):
        h, w = map(int, input().strip().split())
        jail = [[char for char in '.'+input().strip()+'.'] for _ in range(h)]

        # adding boundaries
        jail[:0] = ['.' * (w+2)]
        jail += ['.' * (w+2)]

        solutions.append(jailbreak(h, w, jail))

    for solution in solutions:
        print(solution)
