def find_max(a, b, c):
    return max([a + b + c, a + b * c, a * b + c, a * b * c,
                a * (10 * b + c), (10 * a + b) * c, a + (10 * b + c), (10 * a + b) + c])


while True:
    try:
        a, b, c = [int(x) for x in input().split()]
        print(find_max(a, b, c))
    except EOFError:
        break
