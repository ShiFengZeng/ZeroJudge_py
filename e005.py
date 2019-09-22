import sys
from math import gcd

for coordinate in sys.stdin:
    x1, y1, x2, y2, x3, y3 = [int(x) for x in coordinate.split()]
    if x1 == y1 == x2 == y2 == x3 == y3 == 0:
        break
    dx1 = abs(x1 - x2)
    dy1 = abs(y1 - y2)

    dx2 = abs(x1 - x3)
    dy2 = abs(y1 - y3)

    dx3 = abs(x2 - x3)
    dy3 = abs(y2 - y3)
    count = 0

    if dx1 and dy1:
        count += gcd(dx1, dy1)
    else:  # dx,dy其中一個為0
        count += dy1 if not dx1 else dx1
    if dx2 and dy2:
        count += gcd(dx2, dy2)
    else:
        count += dy2 if not dx2 else dx2
    if dx3 and dy3:
        count += gcd(dx3, dy3)
    else:
        count += dy3 if not dx3 else dx3

    print(count)
