c = [1, 0, 0, 0, 0, 0, 1, 0, 2, 1]
while True:
    try:
        N = input()
        count = 0
        for i in N:
            count += c[int(i)]
        print(count)
    except EOFError:
        break
