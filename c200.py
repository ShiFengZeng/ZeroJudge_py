T = int(input())
for _ in range(T):
    num = input()
    c = 1
    n = 0
    total = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i].isalpha():
            n = ord(num[i]) - ord('A') + 10
        else:
            n = int(num[i])
        total += c * n
        c *= 36

    print(total % 1688 + 1)
