while True:
    try:
        a, op, b = input().split()
        a, b = int(a), int(b)

        if op == '/':
            print(a // b)
        elif op == '+':
            print(a + b)
        elif op == '-':
            print(a - b)
        else:
            print(a * b)

    except EOFError:
        break
