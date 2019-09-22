import sys

s = [0] * 100

for line in sys.stdin:
    if line == '0\n':
        break

    scores = [int(x) for x in sys.stdin.readline().split()]
    for i in scores:
        s[i % 100] += 1

    # m*n           1~49
    # m*(m-1)/2     0 50

    total = (s[0] * (s[0] - 1) // 2) + (s[50] * (s[50] - 1) // 2)
    s[0] = s[50] = 0
    for i in range(1, 50):
        total += s[i] * s[100 - i]
        s[i] = s[100 - i] = 0
    print(total)
