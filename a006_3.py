while 1:
    try:
        a, b, c = [int(x) for x in input().split()]
        D = b * b - 4 * a * c

        if D > 0:
            x1 = int((-b + D ** (1 / 2)) / (2 * a))
            x2 = int((-b - D ** (1 / 2)) / (2 * a))
            print('Two different roots x1={} , x2={}'.format(x1, x2))
        elif D == 0:
            x = int(-b / (2 * a))
            print('Two same roots x={}'.format(x))
        else:
            print('No real root')

    except EOFError:
        break

# str.format #
