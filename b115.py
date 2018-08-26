calc = {'*': lambda a, b: a * b, '/': lambda a, b: a // b}

while True:
    try:
        x = int(input())
        op = input().strip()
        y = int(input())
        print(calc[op](x, y))

    except EOFError:
        break
