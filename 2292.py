# 벌집

# sigma 6t = 3n(n+1)

n = int(input())
cnt = 0
running = True
while running == True:
    if n == 1:
        print(1)
        running = False
    elif 3*cnt*(cnt+1)+1 < n and 3*(cnt+1)*((cnt+1)+1)+1 >= n:
        print(cnt+2)
        running = False
    else:
        cnt += 1
