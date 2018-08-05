while True:
    try:
        T = int(input())
        for i in range(T):
            s = input()
            mul = 1
            for j in s:
                mul *= int(j)
            print(mul)
    except EOFError:
        break
