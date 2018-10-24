from math import sqrt


def area(a, b, c):
    s = (a + b + c) / 2
    if s - a <= 0 or s - b <= 0 or s - c <= 0:
        return 0
    else:
        return sqrt(s * (s - a) * (s - b) * (s - c))


while True:
    try:
        N = int(input())
        for _ in range(N):
            Si = [float(x) for x in input().split()]
            A = sorted(Si[1:])
            Max = 0
            for i in range(0, len(Si) - 3):
                Max = max(area(A[i], A[i + 1], A[i + 2]), Max)
            print("%.2f" % Max)
    except EOFError:
        break
