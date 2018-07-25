while True:
    try:
        line = int(input())
        for i in range(line):
            a, b, c = map(int, input().split())
            print(max(a, b, c))

    except EOFError:
        break
