import sys

N = int(input())
for _ in range(N):
    input()
    M = int(input())
    L = M
    num = [[0 for a in range(2)] for b in range(M)]
    res = [0] * M

    for NUM in sys.stdin:
        M -= 1
        num[M][0], num[M][1] = [int(x) for x in NUM.split()]
        if M == 0:
            break

    temp = num[0][0] + num[0][1]
    res[L - 1] = temp % 10
    temp //= 10
    for i in range(1, L):
        temp = num[i][0] + num[i][1] + temp
        res[L - i - 1] = temp % 10
        temp //= 10

    for i in range(L):
        print(res[i], end="")
    print()
    print()
