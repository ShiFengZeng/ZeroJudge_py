import sys

for num in sys.stdin:
    num = int(num)
    n = bin(num)[2:].zfill(32)
    _1 = int(n[0:8], 2)
    _2 = int(n[8:16], 2)
    _3 = int(n[16:24], 2)
    _4 = int(n[24:32], 2)
    print('%d.%d.%d.%d' % (_1, _2, _3, _4))