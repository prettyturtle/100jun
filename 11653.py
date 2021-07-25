# 소인수분해

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

n = int(input())

if find_prime_number(n) == 1:
    print(n)
else:
    num = n
    prime_num_list = []
    for i in range(2, n + 1):
        if num != 1:
            while num % i == 0:
                prime_num_list.append(i)
                num = num // i
        else:
            break
    prime_num_list.sort()
    for j in prime_num_list:
        print(j)