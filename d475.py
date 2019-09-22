import sys

for line in sys.stdin:
    a, n = map(lambda x: int(x), line.split())
    if a == n == 0:
        count = 0
        for line2 in sys.stdin:
            count += 1
        print('All Over. Exceeded 65536 lines!')  # 測資有誤
        break
    print(int(a ** n))