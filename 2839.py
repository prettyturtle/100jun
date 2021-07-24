# 설탕배달

# N = 3x + 5y => x + y의 최솟값을 구하는 문제

n = int(input())

x = n // 5
reminder_5 = n % 5
y = reminder_5 // 3
while reminder_5 % 3 != 0:
    if x != 0:  
        x -= 1
        reminder_5 += 5
        y = reminder_5 // 3
    else:
        y = -1
        break

print(x + y)



