while True:
    try:
        n = int(input())
        print(2 << n-1)
    except EOFError:
        break