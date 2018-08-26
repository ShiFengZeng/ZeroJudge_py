def calc(a, t, b):
    c = {'+': lambda: a + b, '-': lambda: a - b,
         '*': lambda: a * b, '/': lambda: a // b}
    return c[t]()


while True:
    try:
        x, op, y = input().split()
        x = int(x)
        y = int(y)
        print(calc(x, op, y))

    except EOFError:
        break
