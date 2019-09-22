def dfs(x, y, c):
    if x < 0 or x >= H or y < 0 or y >= W or Map[x][y] != c:
        return
    Map[x][y] = 0
    dfs(x + 1, y, c)
    dfs(x, y + 1, c)
    dfs(x - 1, y, c)
    dfs(x, y - 1, c)


N = int(input())
for n in range(N):
    H, W = [int(x) for x in input().split()]
    Map = [["" for j in range(W)] for i in range(H)]
    for i in range(H):
        temp = input()
        for j in range(W):
            Map[i][j] = temp[j]

    language = {}
    for i in range(H):
        for j in range(W):
            if Map[i][j] is not 0:
                if Map[i][j] in language:
                    language[Map[i][j]] = language[Map[i][j]] + 1
                else:
                    language[Map[i][j]] = 1
                dfs(i, j, Map[i][j])
    print("World #%d" % (n + 1))
    lan = sorted(language.items(), key=lambda a: (-a[1], a[0]))

    for k in lan:
        print(k[0] + ":", k[1])