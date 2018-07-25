while 1:  # True
    try:
        line = input()
        row, col = [int(x) for x in line.split()]
        # row, col = [int(x) for x in input().split()]
        a = [[0 for i in range(col)] for j in range(row)]

        for x in range(row):
            line2 = [int(x) for x in input().split()]
            for y in range(col):
                a[x][y] = line2[y]

        for x in range(col):
            for y in range(row):
                print(a[y][x], end=' ')
            print()
    except EOFError:
        break
