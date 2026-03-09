import sys
input = sys.stdin.readline

rowN, colN = map(int, input().split())
maps = []
for _ in range(rowN):
    maps.append(list(map(int, input().split())))

dp = [[0]*colN for _ in range(rowN)]
dp[0][0] = maps[0][0]
for rowIdx in range(1, colN):
    dp[0][rowIdx] = dp[0][rowIdx-1] + maps[0][rowIdx]

for rowIdx in range(1, rowN):

    right = [0]*colN
    left = [0]*colN

    for colIdx in range(colN):
        if colIdx == 0:
            right[colIdx] = dp[rowIdx-1][colIdx] + maps[rowIdx][colIdx]
            continue

        right[colIdx] = max(right[colIdx-1], dp[rowIdx-1][colIdx]) + maps[rowIdx][colIdx]

    for colIdx in range(colN-1, -1, -1):
        if colIdx == colN-1:
            left[colIdx] = dp[rowIdx-1][colIdx] + maps[rowIdx][colIdx]
            continue

        left[colIdx] = max(left[colIdx+1], dp[rowIdx-1][colIdx]) + maps[rowIdx][colIdx]

    for colIdx in range(colN):
        dp[rowIdx][colIdx] = max(right[colIdx], left[colIdx])

print(dp[rowN-1][colN-1])