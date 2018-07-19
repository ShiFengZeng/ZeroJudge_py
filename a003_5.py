fortune = ('普通', '吉', '大吉')
while True:
    try:
        line = input()
        M, D = line.split()
        M = int(M)
        D = int(D)
        S = (M * 2 + D) % 3

        print(fortune[S])
    except EOFError:
        break
