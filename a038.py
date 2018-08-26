while True:
    try:
        line = input()
        print(int(line[::-1]))
    except EOFError:
        break
