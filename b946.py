# 克拉瑪
# D = a1 * b2 - a2 * b1
# Dx = c1 * b2 - b1 * c2
# Dy = a1 * c2 - a2 * c1
import sys

for i in sys.stdin:
    S1, S2, T, K = [int(x) for x in i.split()]
    D = S1 - S2
    Dx = T - S2 * K
    Dy = S1 * K - T
    x = Dx / D
    y = Dy / D
    if (x.is_integer() and x > 0) and (y.is_integer() and y > 0):
        print(int(x), int(y))
    else:
        print('impossible')
