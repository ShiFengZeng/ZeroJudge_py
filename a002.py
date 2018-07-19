import sys

for line in sys.stdin:
    try:
        a, b = line.split()
        print(int(a) + int(b))
    except EOFError:
        break