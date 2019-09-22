def main():
    table = [[i * j for i in range(1000)] for j in range(50)]

    import sys
    res = []
    append = res.append
    read = sys.stdin.readline
    for s in sys.stdin:
        n = int(s) - 1
        num = [int(x) for x in read().split()]

        m = 0

        if n == 0:
            append('0\n')
            continue

        while n:
            append(str(table[num[m]][n]))
            n -= 1
            m += 1
        append('\n')
    print(' '.join(res))


main()
