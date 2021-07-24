# ACM 호텔

T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    if n % h == 0:
        xx = n // h
        yy = h
    else:
        xx = (n // h) + 1
        yy = n % h
    answer = yy * 100 + xx
    print(answer)
