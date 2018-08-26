while True:
    try:
        n, m = [int(x) for x in input().split()]
        hasSol = False
        for y in range(n, m + 1):
            allAdd = 0
            nLen = len(str(y))

            temp = y
            while temp > 0:
                allAdd += (temp % 10) ** nLen
                temp //= 10
            if allAdd == y:
                print(y, end=' ')
                hasSol = True

        if not hasSol:
            print('none')
        else:
            print()
    except EOFError:
        break
