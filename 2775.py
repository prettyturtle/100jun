# 부녀회장이 될테야

# k층의 n호에 살려면 (k-1)층의 1호부터 n호까지 사람들의 수의 합만큼
# 0층부터 있고 1호부터 있다
# i호에는 i명이 산다

# ex) 1층의 3호 => 0층의 1호부터 3호까지의 사람의 수 = 1 + 2 + 3 = 6
#   0층 : 1, 2, 3, 4, 5, 6, ...
#   1층 : 1, 3, 6, 10, 15, ...
#   2층 : 1, 4, 10, 20, 35, ...
# ex) 2층의 3호 => 1층의 1호부터 3호까지의 사람의 수 = 

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    
    _0_th_floor = [i for i in range( 1, n + 1 )]
    for _ in range(k):
        for j in range( 1, n ):
            _0_th_floor[j] += _0_th_floor[ j - 1 ]
    print(_0_th_floor[-1])
