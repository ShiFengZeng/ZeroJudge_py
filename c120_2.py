while 1:
    ans = 1
    try:
        s = int(input())
        for i in range(2, s + 1):
            ans = ans * i
        print("%d!\n%d" % (s, ans))

        ans = 1

    except EOFError:
        break
