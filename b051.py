from functools import cmp_to_key


def cmp(a, b):
    if a + b < b + a:
        return 1
    elif a + b > b + a:
        return -1
    else:
        return 0


while True:
    try:
        A = []
        A = input().split()[1:]

        A.sort(key=cmp_to_key(cmp))
        print(*A, sep='')
    except EOFError:
        break
