l = [2]
for i in range(3, 1000001):
    flag = True
    for j in l:
        if i % j == 0:
            flag = False
            break
    if flag:
        l.append(i)

while 1:  # True
    try:
        number = int(input())
        isFirstFactor = 1  # True
        i = 0

        while number > 1:
            sameFactorCount = 0
            while number % l[i] == 0:
                number /= l[i]
                sameFactorCount += 1

            if sameFactorCount > 0:
                if isFirstFactor:
                    if sameFactorCount == 1:
                        print(str(l[i]), end='')
                    else:
                        print(str(l[i]) + '^' + str(sameFactorCount), end='')
                    isFirstFactor = 0  # False
                else:
                    if sameFactorCount == 1:
                        print(' * ' + str(l[i]), end='')
                    else:
                        print(' * ' + str(l[i]) + '^' + str(sameFactorCount), end='')
            i += 1

        print()

    except EOFError:
        break
