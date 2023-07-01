# deque: Double-Ended QUEue. Used for implementing stack, queue, etc.
# not actually a queue, strictly speaking; supports both FIFO and LIFO.
from collections import deque
import sys

def bfs():  # breath first search algorithms
  #  print("destination: ", x2, y2)
    while q:                            # while there are cells left to visit
        x, y = q.popleft()
   #     print("current: ", x, y)

        if x == x2 and y == y2:         # and if we've found the other swan
            return True                 # finished!

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and c[nx][ny] == 0:  # unvisited
                    if wc[nx][ny] == 1: # water
                        q.append([nx, ny])          # queue its neighbors
    #                    print("queued:", nx, ny)
                    else:
                        q_temp.append([nx, ny])
                    c[nx][ny] = 1
    return False

def melt(): # defines how the grid changes per "day"; melting ice
    #print()
    #print("[INFO] Melting...")
    #printGrid()
    while wq: # while water cells exist
        x, y = wq.popleft()     # dequeue first water cell
        if grid[x][y] == 'X':
            grid[x][y] = '.'    # update grid; used in BFS

        # calculating next melt: updated after next bfs
        for i in range(4):      # and for each of its adjacent cell
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:         # if it's within grid direction
                if not wc[nx][ny]:
                    if grid[nx][ny] == 'X':
                        wq_temp.append([nx, ny])    # make water
                        #print("[INFO] an ice has melted.")
                    else:
                        wq.append([nx, ny])         # it's already water, add to queue
                    wc[nx][ny] = 1                  # water 1, ice 0
    #print("[INFO] Melted!")
    #printGrid()

def printGrid():
    for i in range(R):
        for j in range(C):
            if i==x1 and j==y1 or i==x2 and j==y2:
                print("L", end="")
            elif wc[i][j] == 1:
                print(".", end="")
            else:
                print("X", end="")
        print()
    print()

# first line of input
R, C = map(int, sys.stdin.readline().split())

c = [[0] * C for _ in range(R)]      # 0 unvisited, 1 visited
wc = [[0] * C for _ in range(R)]     # 0 ice, 1 water

# change in coordinate values for right, left, up, down
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# grid data, swan coordinates
grid, swan = [], []
# queues and temp queues for traverseing, etc
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

# initializing via rest of the input input
for i in range(R):
    row = list(sys.stdin.readline().strip())
    grid.append(row)
    for j, k in enumerate(row):     # j is index, k is value
        if grid[i][j] == 'L':   # swan found
            swan.extend([i, j])
            wc[i][j] = 1
            wq.append([i, j])
        elif grid[i][j] == '.':  # water cell
            wc[i][j] = 1
            wq.append([i, j])

# swan coordinates assigned to values
x1, y1, x2, y2 = swan
q.append([x1, y1])

# swan cells are water
grid[x1][y1], grid[x2][y2], c[x1][y1] = '.', '.', 1
day_num = 0

while True:
    if bfs():   # if swans can meet
        print(day_num)
        break
    melt()      # melt the ice; the swans cannot meet initially
    q, wq = q_temp, wq_temp # update cell state
    q_temp, wq_temp = deque(), deque() # wipe tmp queues
    day_num += 1 # new day!
