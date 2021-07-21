# 달팽이는 올라가고 싶다

a, b, v = map(int, input().split())

goal = v - a

one_day_up = a - b

line_before = (goal // one_day_up)

if (line_before * one_day_up) + a < v:
  print(line_before + 2)
else:
  print(line_before + 1)