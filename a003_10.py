while True:
    try:
        M, D = [int(x) for x in input().split()]
        S = (M * 2 + D) % 3

        if S == 0:
            print("普通")
        elif S == 1:
            print("吉")
        else:
            print("大吉")
    except EOFError:
        break
