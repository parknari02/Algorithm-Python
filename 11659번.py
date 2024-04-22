num, question = map(int, input().split())
numlist = list(map(int, input().split()))
totallist = [0]

for i in range(num):
    newtotal = totallist[i] + numlist[i]
    totallist.append(newtotal)

answer = []
for k in range(question):
    i, j = map(int, input().split())
    answer.append(totallist[j] - totallist[i-1])

for i in answer:
    print(i)