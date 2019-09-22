import sys

ans = []
for s in sys.stdin:
    m, n = [int(x) for x in s.split()]
    if m == n == 0:
        print("".join(ans), end='')
        break
    ans.append(str(m ** n) + '\n')
