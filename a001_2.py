while True:
    try:
        line = input()
        print('hello,', line)
    except EOFError:
        break
