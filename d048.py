def is_palindrome_or_not(h, m):
    if h == 0:
        return m < 10 or m // 10 == m % 10
    elif h < 10:
        return h == m % 10
    else:
        return h // 10 == m % 10 and h % 10 == m // 10


n = int(input())
out = []
for _ in range(n):
    time = [int(x) for x in input().split(':')]
    h = time[0]
    m = time[1]

    m += 1
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0

    while not is_palindrome_or_not(h, m):
        m += 1
        if m == 60:
            h += 1
            m = 0
        if h == 24:
            h = 0
    out.append(str(h // 10) + str(h % 10) + ":" + str(m // 10) + str(m % 10) + "\n")
print("".join(out), end="")
