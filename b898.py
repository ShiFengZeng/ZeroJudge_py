import sys


for s in sys.stdin:
    for i in range(int(s)):
        abc = input()
        a, b, c = abc.split()
        print(max(int(a), int(b), int(c)))
