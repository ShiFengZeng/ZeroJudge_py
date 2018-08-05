import random

UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z']
LOWER = [s.lower() for s in UPPER]

w, v1, v2 = [int(x) for x in input().split()]

times = v1 - 1
for x in range(w):
    s = ''
    s += UPPER[random.randint(0, 25)]
    for y in range(times):
        s += LOWER[random.randint(0, 25)]
        if len(s) >= v2:
            times -= 2

    times += 1
    print('{0}: hello, {0}'.format(s))
