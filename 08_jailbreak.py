from collections import deque
import sys
input = sys.stdin.readline
# Wall = '*', space = '.', door = '#', prisoner = '$'

dyx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def openRegion(h, w, graph):
    visited = [[0 for _ in range(w)] for _ in range(h)]
    q = deque()

    for y in range(h):
        for x in [0, w-1]:
            if map[y][x] != '*':
                q.append(y, x)
    for y in [1, h-1]:
        for x in range(w):
            if map[y][x] != '*':
                q.append(y, x)
    while q:
        cy, cx = q.popleft()
        if map[cy][cx] == '#':
            visited[cy][cx] = 1 # boundary door!
            continue            # can't move anywhere from door w/o opening it!

        count += 1
        for dy, dx in dyx:
            ny, nx = y+dy, x+dx
            if 0 <= ny < h and 0 <= nx < w and map[ny][nx] != '*' and not visited[ny][nx]:
                visited[ny][nx] == 1
                q.append((ny, nx))
    return visited

def toGraph(h, w, map):
    graph = [[] for _ in range(h*w)]
    prisoners = []
    for y in range(h):
        for x in range(w):
            if map[y][x] == '*':
                continue
            if map[y][x] == '$':
                prisoners.append((y, x))
            weight = 1 if map[y][x] == '#' else 0
            for dy, dx in dyx:
                ny, nx = y+dy, x+dx
                if 0 <= ny < h and 0 <= nx < w and map[ny][nx] != '*':
                    # flatten ny, nx
                    graph[w*y + x].append((w*ny + nx, weight))
    return graph

def jailbreak(h, w, map):
    openR = openRegion(h, w, map)
    graph = toGraph(map)
    # implement
    return

if __name__ == "__main__":
    testcase = int(input())

    for i in range(testcase):
        h, w = map(int, input().strip().split())
        map = [[char for char in input().strip()] for _ in range(h)]
        sol = jailbreak(h, w, map)
        print(sol)
