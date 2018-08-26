calc = {'+': lambda a, b: a + b, '-': lambda a, b: a - b,
        '*': lambda a, b: a * b, '/': lambda a, b: a // b}

while True:
    try:
        x, op, y = input().split()
        x = int(x)
        y = int(y)
        print(calc[op](x, y))

    except EOFError:
        break
