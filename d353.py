import sys

S = [[] for i in range(31)]
S[0].append(1)
S[1].append(1)
S[1].append(1)
for i in range(1, 30):
    n = 0
    while n < len(S[i]):
        num = S[i][n]
        count = 1
        while (n + 1) < len(S[i]) and num == S[i][n + 1]:
            count += 1
            n += 1
        S[i + 1].append(count)
        S[i + 1].append(num)
        n += 1

for n in sys.stdin:
    ans = map(lambda s: str(s), S[int(n)])
    print("".join(ans))