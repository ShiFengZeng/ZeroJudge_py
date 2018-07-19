def fortune(s):
    return {0: '普通', 1: '吉', 2: '大吉'}.get(s)


while True:
    try:
        line = input()
        M, D = line.split()
        M = int(M)
        D = int(D)
        S = (M * 2 + D) % 3

        print(fortune(S))
    except EOFError:
        break
