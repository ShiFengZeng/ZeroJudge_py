t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    count = 0
    while n > 1:
        n = n - m + 1
        count += 1
    if n == 1:
        print(count)
    else:
        print('cannot do this')
