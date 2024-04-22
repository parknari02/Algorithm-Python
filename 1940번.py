import sys
input = sys.stdin.readline

n = int(input())
sum_num = int(input())
ingredients = list(map(int, input().split()))
ingredients.sort()
start = 0
end = len(ingredients) - 1
count = 0

while(start != end):
    if ( ingredients[start] + ingredients[end] < sum_num):
        start = start + 1
    elif (ingredients[start] + ingredients[end] == sum_num):
        count = count + 1
        start = start + 1
    else:
        end = end - 1

print(count)