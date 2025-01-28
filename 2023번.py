#신기한 소수 찾기
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N = int(input())


def findPrimeNumber(n):
    for i in range(2, int(n / 2 + 1)):
        if(n % i == 0):
            return False
    return True

def DFS(num):
    if (len(str(num)) == N):
        print(num)
    else:
        for i in range(1, 10, 2):
            if ( i % 2 == 0):
                continue
            if findPrimeNumber(num * 10 + i):
                DFS(num * 10 + i) 
            
            
DFS(2)
DFS(3)
DFS(5)
DFS(7)


