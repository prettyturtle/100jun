# 분수찾기

# cnt+1이 짝수일때 위로 올라가는 방향
# 계차수열
# init, cnt

n = int(input())
init = 1
cnt = 1
running = True
while running == True:
    if n <= init:
        running = False
    else:
        cnt += 1
        init += cnt

num_list = [i for i in range(init - (cnt - 1), init + 1)]
if (cnt) % 2 == 0:
    num_list.reverse()
else:
    num_list.sort()
n_index = num_list.index(n) + 1
print('{}/{}'.format(cnt+1-n_index, n_index))