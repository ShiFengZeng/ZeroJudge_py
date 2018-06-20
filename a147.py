import sys

for n in sys.stdin:
    if int(n) == 0:
        break
    for i in range(1, int(n)):
        if int(i) % 7 == 0:
            continue
        else:
            print(i, end=' ')
    print()
