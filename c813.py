import sys


def f(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


for line in sys.stdin:
    line = int(line)
    if line == 0:
        break
    while line >= 10:
        line = f(line)
    print(line)
