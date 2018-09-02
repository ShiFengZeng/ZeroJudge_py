while True:
    try:
        mushroom = [int(x) for x in input().split()]
        theSum = theMax = 0
        for i in range(1, mushroom[0] + 1):
            theSum += mushroom[i]
            theSum = max(0, theSum)
            theMax = max(theMax, theSum)
        print(theMax)
    except EOFError:
        break
