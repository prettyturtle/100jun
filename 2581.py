# 소수

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

m = int(input())
n = int(input())

prime_number_list = []
for i in range( m, n + 1 ):
    if find_prime_number(i) == 1:
        prime_number_list.append(i)

if len(prime_number_list) != 0:
    prime_number_list.sort()
    print(sum(prime_number_list))
    print(prime_number_list[0])
else:
    print(-1)



