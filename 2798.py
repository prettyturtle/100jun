# 블랙잭

n, m = map(int,input().split())

card_list = list(map(int, input().split()))

three_sum_list = []

for i in range(len(card_list)-2):
    for j in range(i + 1, len(card_list)-1):
        for k in range(j + 1, len(card_list)):
            three_sum_list.append(card_list[i] + card_list[j] + card_list[k])

three_sum_list = list(set(three_sum_list))
three_sum_list.sort()
answer = []
for num in three_sum_list:
    if num <= m:
        answer.append(num)

print(max(answer))