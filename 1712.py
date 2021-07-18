# 손익분기점

# A = 고정비용
# B = 가변비용
# C = 수입

# '''
# 손익 분기점 = {고정비용 / (수입 - 가변비용)} + 1
# '''

a, b, c = map(int, input().split())

if b >= c:
  print(-1)
else:
  break_even_point = (a / (c - b)) + 1
  print(int(break_even_point))

