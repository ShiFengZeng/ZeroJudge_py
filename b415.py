import sys

for line in sys.stdin.buffer:
    x, n, m = (int(a) for a in line.split())
    m -= 1
    out = list()
    out.append(str(x))
    for _ in range(m):
        x = (x * x) % n
        out.append(" " + str(x))
    res = "".join(out)
    print(res)
