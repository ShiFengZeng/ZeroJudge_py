while True:
    try:
        applesHeight = [int(x) for x in input().split()]
        height = int(input()) + 30
        count = 0
        for h in applesHeight:
            if height >= h:
                count += 1
        print(count)
    except EOFError:
        break
