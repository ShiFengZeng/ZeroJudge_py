while True:
    try:
        n = int(input())
        nums = [int(x) for x in input().split()]
        digit = dict()
        for i in nums:
            if i not in digit:
                digit[i] = 1
            else:
                digit[i] = digit.get(i) + 1
        d = sorted(digit.items(), key=lambda a: (-a[1], a[0]))

        for i in d:
            print(i[0], end=" ")
        print()
    except EOFError:
        break
