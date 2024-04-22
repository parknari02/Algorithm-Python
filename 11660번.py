import sys
input = sys.stdin.readline

arraySize, questions = map(int, input().split())
doubleArray = []
sumArray = [[0] * (arraySize + 1)]

for _ in range(arraySize):
    sumArray.append([0])

for _ in range(arraySize):
    n = list(map(int, input().split()))
    doubleArray.append(n)


for i in range(1, arraySize+1):
    for j in range(1, arraySize+1):
        if i == 1:
            sumnum = sumArray[i][j-1] + doubleArray[i-1][j-1] 
            sumArray[i].append(sumnum)

        elif i != 1 and j == 1:
            sumnum = sumArray[i-1][j] + doubleArray[i-1][0]
            sumArray[i].append(sumnum)
        else:
            sumnum = sumArray[i][j-1] + sumArray[i-1][j] + doubleArray[i-1][j-1] - sumArray[i-1][j-1]
            sumArray[i].append(sumnum)


for _ in range(questions):
    x1, y1, x2, y2 = map(int, input().split())
    answer = sumArray[x2][y2] - sumArray[x1-1][y2] - sumArray[x2][y1-1] + sumArray[x1-1][y1-1]
    print(answer)


