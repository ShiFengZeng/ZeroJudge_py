def move(n, a, b, c):
    if n == 1:
        print("Move ring %d from %s to %s" % (n, a, c))
    else:
        move(n - 1, a, c, b)
        print("Move ring %d from %s to %s" % (n, a, c))
        move(n - 1, b, a, c)


while True:
    try:
        N = int(input())
        move(N, 'A', 'B', 'C')

    except EOFError:
        break
