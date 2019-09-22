T = int(input())
for i in range(1, T + 1):
    input()
    A = input()

    index = 0
    ans = 0
    while index < len(A):
        if A[index] == '.':
            ans += 1
            index += 3
        else:
            index += 1
    print('Case {}: {}'.format(i, ans))
