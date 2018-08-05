while True:
    try:
        a = int(input())
        print(int(a * 0.3))
    except EOFError:
        break
