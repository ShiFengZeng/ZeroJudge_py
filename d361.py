ans = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]
temp = []
while True:
    m, n = [int(x) for x in input().split()]
    if m == n == 0:
        print("".join(temp))
        break
    elif m != 0 and n == 0:
        temp.append(str(1) + '\n')
    else:
        a = ans[int(str(m)[-1])]
        temp.append(str(a[((n - 1) % len(a))]) + '\n')
