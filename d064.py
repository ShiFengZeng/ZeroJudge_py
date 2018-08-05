while True:
    try:
        i = int(input())
        if i % 2 == 1:
            print('Odd')
        else:
            print('Even')
    except EOFError:
        break
