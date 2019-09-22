N = int(input())
for _ in range(N):
    X, a, b = [int(x) for x in input().split()]
    quotient = X // a
    total = 99999
    for i in range(quotient, -1, -1):
        c = X - i * a
        if c % b == 0:
            quotient2 = c // b
            total = min(total, (i + quotient2))
    if total == 99999:
        print(-1)
    else:
        print(total)