def cal():
    global x
    global y
    global op
    return {'+': x + y, '-': x - y, '*': x * y, '/': x // y}[op]


while True:
    try:
        x, op, y = input().split()
        x, y = int(x), int(y)
        print(cal())
    except EOFError:
        break
