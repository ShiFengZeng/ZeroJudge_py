fortune = {0: '普通', 1: '吉', 2: '大吉'}
while True:
    try:
        line = input()
        M, D = line.split()
        M = int(M)
        D = int(D)
        S = (M * 2 + D) % 3

        print(fortune.get(S))
    except EOFError:
        break
