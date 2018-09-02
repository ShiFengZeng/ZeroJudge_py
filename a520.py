while True:
    try:
        s = input()
        spaceCount = maxSpaceCount = 0
        for i in s:
            if i == ' ':
                spaceCount += 1
            else:
                maxSpaceCount = max(spaceCount, maxSpaceCount)
                spaceCount = 0

        count = 0
        while maxSpaceCount > 1:
            count += 1
            maxSpaceCount = sum(divmod(maxSpaceCount, 2))
        print(count)
    except EOFError:
        break
