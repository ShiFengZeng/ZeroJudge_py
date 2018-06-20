import sys

ans = 1
for s in sys.stdin:
    s = s.strip('\n')
    for i in range(2, int(s) + 1):
        ans = ans * i
    print("%s!" % s)
    print(ans)
    ans = 1
