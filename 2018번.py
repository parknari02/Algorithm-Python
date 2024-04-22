import sys
input = sys.stdin.readline

n = int(input())

sum = 0
count = 0
start_index = 0
end_index = 0

while(end_index < n):
    if sum < n:
        sum = sum + (end_index + 1)
        end_index = end_index + 1
    elif sum == n:
        count = count + 1
        sum = sum + (end_index + 1)
        end_index = end_index + 1
    else:
        sum = sum - (start_index + 1)
        start_index = start_index + 1

print(count+1)



