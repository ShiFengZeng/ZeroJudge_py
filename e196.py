n, m = [int(x) for x in input().split()]
p = [0] * (n + 1)
r = [int(x) for x in input().split()]
for i in r:
    p[i] += 1
c = 0
for i in range(1, n + 1):
    if p[i] != 2:
        c += 1
print(c)
