while True:
    try:
        a, op, b = input().split()
        a = int(a)
        b = int(b)
        if op == '+':
            print((lambda x, y: x + y)(a, b))
        elif op == '-':
            print((lambda x, y: x - y)(a, b))
        elif op == '*':
            print((lambda x, y: x * y)(a, b))
        else:
            print((lambda x, y: x // y)(a, b))
    except EOFError:
        break
