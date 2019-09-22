while 1:
    try:
        input()
        scores = [int(x) for x in input().split()]

        Max = 0
        for i in scores:
            if i > Max:
                Max = i

        print(Max)
    except EOFError:
        break
