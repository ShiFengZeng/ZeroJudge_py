def cal(inp):
    c = 0
    for i in inp:
        if c < 0:
            return False
        if i == 'Y':
            c += 1
        else:
            c -= 1
    if c == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    while 1:
        try:
            n = int(input())
            for _ in range(n):
                print('YES' if cal(input()) else 'NO')
        except EOFError:
            break
