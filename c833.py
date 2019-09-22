N, M = [int(x) for x in input().split()]
X = [0] * N
Y = [0] * M

for i in range(N):
    a = input()
    for j in range(M):
        if a[j] == '#':
            X[i] = 1
            Y[j] = 1

temp = []
res = ""

for i in range(N):
    for j in range(M):
        if X[i] == 1 or Y[j] == 1:
            temp.append('#')
        else:
            temp.append('X')
    temp.append('\n')
res = "".join(temp)
print(res)
