T = int(input())
for i in range(T):
    n, m = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A.sort()

    print('Case ' + str(i + 1) + ':')
    for j in range(m):
        a = [int(x) for x in input().split()]
        if a[0] == 1:
            A.append(a[1])
            n += 1
            A.sort()
        else:
            if n > 0:
                print("Max:", A.pop())
                n -= 1
            else:
                print("It's empty!")
    if n > 0:
        while len(A) > 0:
            print(A.pop(), end=" ")
        print()
    else:
        print("It's empty!")
