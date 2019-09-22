while 1:
    try:
        number = int(input())
        if number == 0:
            print(0)
        else:
            print((number - 1) % 9 + 1)
    except EOFError:
        break
