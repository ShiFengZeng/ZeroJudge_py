T = int(input())
for i in range(T):
    n, m = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A.sort()

    print('Case ' + str(i + 1) + ':')
    a = [0] * m
    for j in range(m):
        a[j] = [int(x) for x in input().split()]

    for j in range(m):
        if a[j][0] == 1:
            A.append(a[j][1])
            n += 1
        else:
            if a[j - 1][0] == 1:
                A.sort()

            if n > 0:
                print("Max:", A.pop())
                n -= 1
            else:
                print("It's empty!")
    if n > 0:
        A.sort()
        while n > 0:
            print(A.pop(), end=" ")
            n -= 1
        print()
    else:
        print("It's empty!")