while True:
    try:
        line = input()
        K = 7
        for asc in line:
            c = chr(ord(asc) - K)
            print(c, end='')
        print()
    except EOFError:
        break
