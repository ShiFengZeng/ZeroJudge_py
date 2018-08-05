while True:
    try:
        t = int(input())

        for x in range(1, t + 1):
            a = int(input())
            b = int(input())
            abSum = 0

            for i in range(int(a ** (1 / 2)), int(b ** (1 / 2)) + 1):
                if (i * i >= a) and (i * i <= b):
                    abSum += i * i
            print('Case', str(x) + ':', abSum)
    except EOFError:
        break
