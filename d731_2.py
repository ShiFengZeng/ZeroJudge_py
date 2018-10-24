from functools import cmp_to_key


def cmp(a, b):
    if abs(a) > abs(b):
        return 1
    else:
        return -1


while 1:
    try:
        p = int(input())
        for _ in range(p):
            n = int(input())
            areas = [0] * n
            for i in range(n):
                areas[i] = int(input())
            areas.sort(key=cmp_to_key(cmp))

            index = 0
            count = 1
            for j in range(n):
                if areas[j] * areas[index] < 0:
                    count += 1
                    index = j
            print(count)
    except EOFError:
        break
