#DFS와 BFS 프로그램
from collections import deque
N, M, Start = map(int, input().split())
A = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N+1):
    A[i].sort()


def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if (visited[i] == False):
            DFS(i)

visited = [False] * (N+1)
DFS(Start)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in A[now_Node]:
            if (visited[i] == False):
                visited[i] = True
                queue.append(i)

print()
visited = [False] * (N+1)
BFS(Start)
