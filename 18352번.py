#특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
A = [[]for _ in range(N+1)]
answer = []
visited = [-1] * (N+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        nowNode = queue.popleft()
        for i in A[nowNode]:
            if visited[i] == -1:
                visited[i] = visited[nowNode] + 1
                queue.append(i)

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)

BFS(X)

for i in range(N+1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)