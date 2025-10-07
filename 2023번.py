import sys, math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def DFS(number, length):
    if length == N:
        print(number)
        return
    
    for i in range(1, 10, 2):  # 홀수만 붙이기 (짝수는 소수 안됨)
        next_num = number * 10 + i
        if isPrime(next_num):
            DFS(next_num, length + 1)

# 1자리 소수부터 시작
for start in [2, 3, 5, 7]:
    DFS(start, 1)