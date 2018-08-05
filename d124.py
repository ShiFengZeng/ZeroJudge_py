while True:
    try:
        a = int(input())
        if a % 3 == 0:
            print('yes')
        else:
            print('no')
    except EOFError:
        break
