# 소수 구하기
import math

m, n = map(int, input().split())

def find_prime_number(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

for i in range(m, n + 1):
    if find_prime_number(i) == True:
        print(i)

