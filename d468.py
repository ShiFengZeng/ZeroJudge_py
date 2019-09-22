import sys

for line in sys.stdin:
    a, n = map(lambda x: int(x), line.split())
    if a == n == 0:
        print('All Over.')
        break
    else:
        print(int(a ** n))