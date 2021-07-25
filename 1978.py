# 소수 찾기

n = int(input())

num_li = input().split()
if '1' in num_li:
    num_li.remove('1')

def find_prime_number(a):
    idx = 0
    if a == 1:
        return 0
    else:
        for i in range(2, a):
            if a % i == 0:
                idx = -1
                break
            else:
                continue
        if idx == -1:
            return 0
        else:
            return 1

cnt = 0
for num in num_li:
    num = int(num)
    if find_prime_number(num) == 1:
        cnt += 1
    else:
        continue
print(cnt)


