while True:
    try:
        t = int(input())
        for x in range(t):
            a = input()
            M = 0
            F = 0
            for y in a:
                if y == 'M':
                    M += 1
                elif y == 'F':
                    F += 1
            if M > 1 and M == F:
                print('LOOP')
            else:
                print('NO LOOP')

    except EOFError:
        break
