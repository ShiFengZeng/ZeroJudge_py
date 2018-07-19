while 1:  # True
    try:
        number = int(input())
        isFirstFactor = 1  # True
        factor = 2

        while number > 1:
            sameFactorCount = 0
            while number % factor == 0:
                number /= factor
                sameFactorCount += 1

            if sameFactorCount > 0:
                if isFirstFactor:
                    if sameFactorCount == 1:
                        print(str(factor), end='')
                    else:
                        print(str(factor) + '^' + str(sameFactorCount), end='')
                    isFirstFactor = 0  # False
                else:
                    if sameFactorCount == 1:
                        print(' * ' + str(factor), end='')
                    else:
                        print(' * ' + str(factor) + '^' + str(sameFactorCount), end='')
            factor += 1

        print()

    except EOFError:
        break
