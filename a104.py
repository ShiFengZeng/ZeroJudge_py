while 1:
    try:
        n = input()
        A = [int(i) for i in input().split()]
        A.sort()
        print(*A)
    except EOFError:
        break
