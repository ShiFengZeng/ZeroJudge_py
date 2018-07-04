while True:
    try:
        n = int(input())
        for i in range(n):
            line = input()
            a, b, c, d = line.split()
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)

            add1 = b - a
            add2 = c - b
            mul1 = int(b / a)
            mul2 = int(c / b)

            if add1 == add2:
                e = d + add1
            else:
                e = d * mul1

            print(a, b, c, d, e)
    except EOFError:
        break
