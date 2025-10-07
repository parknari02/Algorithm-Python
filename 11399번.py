N = int(input())
A = list(map(int, input().split()))
A.sort()

sum = 0
count = N 
for i in range(N):
    sum += A[i] * count
    count -= 1

print(sum)
