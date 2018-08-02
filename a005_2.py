while 1:
    try:
        n = int(input())
        while n:
            a, b, c, d = [int(x) for x in input().split()]

            add1 = b - a
            add2 = c - b
            mul1 = b // a
            # mul2 = c // b   沒用到 OuO

            if add1 == add2:
                e = d + add1
            else:
                e = d * mul1
            n -= 1
            print(a, b, c, d, e)
    except EOFError:
        break
