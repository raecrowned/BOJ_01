import sys
input = sys.stdin.readline

# keep a stack of increasing indexes that increases in height
# if current height doesn't fit in,
# pop the stack and calculate the "highest" rectangle within the stacked range
# (that is, pop until the stack conditions are met again;
# the last popped item is the highest within the stack by def.)

# After the above, add current to stack, then rinse & repeat.

def largestRect(hist):
    n, area, histStack = len(hist), 0, []
    for idx, height in enumerate(hist): # enumerate() returns idx, element pair

        # not empty and current height less than or equal to top of stack
        while histStack and height <= hist[histStack[-1]]:
            popped = histStack.pop()
            # "-1" operation exists because idx itself isn't included in width
            width = idx if not histStack else idx - histStack[-1] - 1
            area = max(area, hist[popped] * width)

        # must always happen; just not before stack consideration.
        histStack.append(idx)

    # post-process cleanup
    while histStack:
        popped = histStack.pop()
        width = n if not histStack else n - histStack[-1] - 1
        area = max(area, hist[popped] * width)

    return area


if __name__ == "__main__":
    sol = []
    while True:
        # extended unpacking via "splat" prefix '*'
        size, *hist = list(map(int, input().strip().split()))
        if size == 0:
            break
        sol.append(largestRect(hist))
    for solution in sol:
        print(solution)
