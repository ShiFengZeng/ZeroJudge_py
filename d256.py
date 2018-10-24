T = int(input())
for i in range(T):
    G, L = [int(x) for x in input().split()]
    if L % G == 0:
        print(G, L)
    else:
        print(-1)
