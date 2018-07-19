while 1:
    try:
        number = int(input())
        isFirstFactor = 1
        output = ''
        factor = 2

        while number > 1:
            sameFactorCount = 0
            while number % factor == 0:
                number /= factor
                sameFactorCount += 1

            if sameFactorCount > 0:
                if isFirstFactor:
                    if sameFactorCount == 1:
                        output += str(factor)
                    else:
                        output += str(factor) + '^' + str(sameFactorCount)
                    isFirstFactor = 0
                else:
                    if sameFactorCount == 1:
                        output += ' * ' + str(factor)
                    else:
                        output += ' * ' + str(factor) + '^' + str(sameFactorCount)
            factor += 1
        print(output)

    except EOFError:
        break
