import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numlist = list(map(int, input().split()))
sumlist = [numlist[0]]
reminderlist = [0] * M
answer = 0

for i in range(1, N):
    sumlist.append(sumlist[i-1] + numlist[i])

for j in range(N):
    reminder = sumlist[j] % M
    if reminder == 0:
        answer = answer + 1
    reminderlist[reminder] = reminderlist[reminder] + 1
    
for k in range(M):
    if (reminderlist[k]):
        answer = answer + ((reminderlist[k] * (reminderlist[k] - 1)) // 2 )

print(answer)