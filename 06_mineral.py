from collections import deque
import sys
input = sys.stdin.readline

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# takes the currnet round
# breaks the mineral and returns coordinates if stick hits one
# returns [-1, -1] if not hit
def throwStick(iter):
    row = R-throws[iter]
    if iter%2 == 0:
        column, direction = 0, 1
    else:
        column, direction = C-1, -1

    while 0 <= column < C:
        if cave[row][column] == 'x':
            cave[row][column] = '.'
            return [row, column]
        column += direction
    return [-1, -1]

# takes a mineral cell as input
# returns its cluster as list of coordinates
def checkCluster(y, x):
    stable = False
    cluster = [[0] * C for _ in range(R)]
    q = deque([(y, x)])
    cluster[y][x] = 1

    while q:
        y, x = q.popleft()
        if y == R-1:            # if current cell is ground level
            stable = True       # cluster is stable! no need to complete it...
            return stable, None
        # checking neighbors...
        for dy, dx in dxy:
            ny, nx = y+dy, x+dx
            # out of bounds, not a mineral, or already checked
            if not (0 <= ny < R and 0 <= nx < C) or cave[ny][nx] == '.' or cluster[ny][nx]:
                continue
            # [ny][nx] is an unchecked mineral cell: check it
            q.append((ny, nx))
            cluster[ny][nx] = 1
    return stable, cluster      # only unstable clusters are completely checked

# takes an unstable cluster
# drops it
def clusterDrop(cluster):
    unstableLow = [None] * C
    firstAvailable = [R-1] * C
    fallingHeight = [None] * C

    for c in range(C):
        found_unstable = False
        for r in range(R):      # climbing down; 0 is top row
            if cluster[r][c]:
                cave[r][c] = '.'        # found new unstable mineral
                unstableLow[c] = r      # update
                found_unstable = True
            if found_unstable and cave[r][c] == 'x':     # found first available space below unstable cluster
                firstAvailable[c] = r-1                  # add the first space above it.
                break

        if unstableLow[c] is not None:
            fallingHeight[c] = firstAvailable[c] - unstableLow[c]
        else:
            fallingHeight[c] = R        # potential maximum
    dropHeight = min(fallingHeight)

    for c in range(C):
        for r in range(R):
            if cluster[r][c]:
                cave[r+dropHeight][c] = 'x'

def printCave():
    for i in range(R):
        print(''.join(cave[i]))

if __name__ == "__main__":
    R, C = map(int, input().strip().split())
    cave = [[char for char in input().strip()] for _ in range(R)]
    n = int(input())
    throws = [*map(int, input().strip().split())]

    for i in range(n):
        y, x = throwStick(i)
        if y == -1:
            continue
        for dy, dx in dxy:
            ny, nx = y+dy, x+dx
            if not (0 <= ny < R and 0 <= nx < C):   # out of bounds
                continue
            if cave[ny][nx] == 'x':
                stable, cluster = checkCluster(ny, nx)
                if not stable:
                    clusterDrop(cluster)
                    break                   # only one cluster drops for every iteration
    printCave()
