import math

while True:
    try:
        line = int(input())
        line2 = int(input())
        print(math.gcd(line, line2))

    except EOFError:
        break
