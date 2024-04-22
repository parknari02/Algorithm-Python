import sys
input = sys.stdin.readline

n = int(input())
numlist = list(map(int, input().split()))

count = 0
numlist.sort()

for initial_index in range(n):
    find = numlist[initial_index]
    start_index = 0
    end_index = n - 1
    while(start_index < end_index):
        if(numlist[start_index] + numlist[end_index] == find):
            if start_index != initial_index and end_index != initial_index:
                count = count + 1
                break
            elif start_index == initial_index:
                start_index = start_index + 1
            elif end_index == initial_index:
                end_index = end_index -1
        elif(numlist[start_index] + numlist[end_index] < find):
            start_index = start_index + 1
        else:
            end_index = end_index - 1

print(count)