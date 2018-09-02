fortune = {0: '普通', 1: '吉', 2: '大吉'}
while True:
    try:
        M, D = [int(x) for x in input().split()]
        S = (M * 2 + D) % 3

        print(fortune.get(S))
    except EOFError:
        break
