from math import gcd

N = int(input())
for i in range(1, N + 1):
    S1 = int(input(), 2)
    S2 = int(input(), 2)
    L = gcd(S1, S2)
    if L == 1:
        print('Pair #{}: Love is not all you need!'.format(i))
    else:
        print('Pair #{}: All you need is love!'.format(i))
