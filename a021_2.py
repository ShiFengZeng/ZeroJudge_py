def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a // b


op_dict = {'+': add, '-': sub, '*': mul, '/': div}
while True:
    try:
        x, op, y = input().split()
        x = int(x)
        y = int(y)
        print(op_dict[op](x, y))
    except EOFError:
        break
