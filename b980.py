import sys

for line in sys.stdin:
    inp = [int(x) for x in line.split()]
    N = inp[0]
    money = inp[1:-1]
    money.sort(reverse=True)

    m = 0
    for i in range(N):
        if i == len(money):
            break
        m += money[i]
    print(m)