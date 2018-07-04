while True:
    try:
        line = input()
        a, b = line.split()
        print(int(a) + int(b))
    except EOFError:
        break
