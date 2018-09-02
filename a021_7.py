def cal(x, op, y):
    return {'+': x + y, '-': x - y, '*': x * y, '/': x // y}[op]


while True:
    try:
        x, op, y = input().split()
        x, y = int(x), int(y)
        print(cal(x, op, y))
    except EOFError:
        break
