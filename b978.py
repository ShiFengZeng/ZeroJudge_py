while True:
    try:
        s = input()
        order = [int(x) for x in input().split()]
        res_list = [''] * len(s)

        for i in range(len(s)):
            res_list[(order[i] - 1)] = s[i]

        res = "".join(res_list)
        print(res)
    except EOFError:
        break
