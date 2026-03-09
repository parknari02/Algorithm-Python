import sys
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))

INF = float('inf')
start = 0
end = 0
sum = lst[start]
answer = INF

while end < N:
    if sum >= S:
        answer = min(answer, end - start + 1)
        sum -= lst[start]
        start += 1
    else:
        if end == N -1:
            break
        end += 1
        sum += lst[end]
        
if answer != INF:
    print(answer)
else:
    print(0)