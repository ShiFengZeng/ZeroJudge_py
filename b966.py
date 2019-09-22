def do():
    import sys
    for line in sys.stdin:
        ab = []
        cnt = 0
        n = int(line)
        for i in range(n):
            a, b = [int(x) for x in input().split()]
            ab.append([a, b])
        ab.sort(key=lambda x: (x[0], -x[1]))

        i = 0
        while i < n:
            s, e = ab[i][0], ab[i][1]
            while (i + 1) < n and ab[i + 1][0] < e:
                if ab[i + 1][1] <= e:
                    i = i + 1
                else:
                    e = ab[i + 1][1]
                    i = i + 1
            cnt = cnt + e - s
            i = i + 1
        print(cnt)


do()
