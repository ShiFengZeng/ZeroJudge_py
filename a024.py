def gcd(x, y):
    while y > 0:
        temp = x % y
        x = y
        y = temp
    return x


while 1:
    try:
        line = input()
        a, b = line.split()
        print(gcd(int(a), int(b)))

    except EOFError:
        break
