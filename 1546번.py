n = int(input())
score_list = input().split()
new_score_list = []

for i in score_list:
    new_score_list.append(int(i))

m = max(new_score_list)

for i in range(n):
    new_score_list[i] = new_score_list[i] / m * 100

print(sum(new_score_list)/n)