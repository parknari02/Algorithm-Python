#스택으로 수열 만들기
N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i] #주어진 수열에서 어떤 수
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop() #현재 스택의 마지막
        if n > su:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)