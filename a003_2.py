while True:
    try:
        line = input()
        M, D = line.split()
        M = int(M)
        D = int(D)
        S = (M * 2 + D) % 3

        if S == 0:
            print("普通")
        elif S == 1:
            print("吉")
        else:
            print("大吉")
    except EOFError:
        break
