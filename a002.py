import sys

for line in sys.stdin:
    try:
        a, b = line.split()
        a = int(a)
        b = int(b)
        print(a + b)
    except EOFError:
        break
