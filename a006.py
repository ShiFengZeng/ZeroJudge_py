import math

while True:
    try:
        line = input()
        a, b, c = line.split()
        a = int(a)
        b = int(b)
        c = int(c)
        D = b * b - 4 * a * c

        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            print('Two different roots x1=%d , x2=%d' % (x1, x2))
        elif D == 0:
            x = -b / (2 * a)
            print('Two same roots x=%d' % x)
        else:
            print('No real root')

    except EOFError:
        break

# %-formatting #
