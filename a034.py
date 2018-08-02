while 1:
    try:
        line = int(input())
        print(bin(line)[2:])

    except EOFError:
        break
