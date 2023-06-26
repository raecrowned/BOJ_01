def knapsackTry(n, weight, value, maxWeight):
    dp = [[0] * (maxWeight+1) for _ in range(n+1)]

    for i in range(1, n+1): # item# from 1 to n
        for w in range(1, maxWeight+1): # weight limit from 1 to maxWeight
            if weight[i-1] <= w:    # if item within current weight limit
            # calculate the max value achievable and update dp
                dp[i][w] = max(value[i-1]+dp[i-1][w-weight[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][maxWeight]

# map(function, iterable) ==> returns iterators
N, K = map(int, input().split())
weight, value = [0]*N, [0]*N
for i in range(N):
    weight[i], value[i] = map(int, input().split())

print(knapsackTry(N, weight, value, K))
