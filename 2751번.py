import sys
input = sys.stdin.readline
priint = sys.stdin.write
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

A.sort()

for i in A:
    print(i)