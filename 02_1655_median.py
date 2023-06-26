import sys
import heapq    # always min-Heap; negate for max-Heap

N = int(sys.stdin.readline())
smaller = []    # max Heap: parent greater than children
larger = []     # min Heap: parent less than children

for _ in range(N):
    value = int(sys.stdin.readline())
    if len(smaller) == 0 or value < -smaller[0]:    # smaller[0] (root) is max value of the smaller half
        heapq.heappush(smaller, -value)     # value negated
    else:
        heapq.heappush(larger, value)

# balancing: two heaps should always be at most 1 element different in size
    if len(smaller) > len(larger) +1:
        heapq.heappush(larger, -heapq.heappop(smaller))
    elif len(larger) > len(smaller) +1:
        heapq.heappush(smaller, -heapq.heappop(larger))

#    print("smaller: ", smaller)
#    print("larger: ", larger)
# always debug!!!

    if len(smaller) < len(larger):  # odd number of inputs and middle value is larger root
        print(larger[0])
    else:
        print(-smaller[0])          # all other case: median/lesser middle value is smaller root

# heaps are often used for implementing p-queues: "float up" based on priority (min/max in this case!)
