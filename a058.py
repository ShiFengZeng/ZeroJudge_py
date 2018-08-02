while 1:
    _3k = 0
    _3k1 = 0
    _3k2 = 0

    try:
        line = int(input())

        while line:
            n = int(input())

            if n % 3 == 0:
                _3k += 1
            elif n % 3 == 1:
                _3k1 += 1
            else:
                _3k2 += 1
            line -= 1

        print(_3k, _3k1, _3k2)
    except EOFError:
        break
