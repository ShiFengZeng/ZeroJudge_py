def cal(a):
    for i in range(len(a) - 1):
        a[i] = a[i] + a[i + 1]
    return a[:-1]


n = int(input())
a = []
for i in range(1, n + 1):
    a.append(i)
while len(a) > 1:
    a = cal(a)
print(*a)