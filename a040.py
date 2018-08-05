while True:
    try:
        n, m = [int(x) for x in input().split()]
        hasSol = False
        for y in range(n, m + 1):
            str_y = str(y)
            result = 0

            for z in range(len(str_y)):
                result += int(str_y[z]) ** len(str_y)
            if result == y:
                print(result, end=' ')
                hasSol = True

        if not hasSol:
            print('none')
        else:
            print()
    except EOFError:
        break
