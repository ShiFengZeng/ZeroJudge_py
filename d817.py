while True:
    try:
        n = int(input())
        print(2 ** n)
    except EOFError:
        break
