while True:
    try:
        n, t = [int(x) for x in input().split()]

        team = dict()
        for i in range(1, t + 1):
            team[i] = 0

        for i in range(n):
            time = input().split()
            for j in range(1, t + 1):
                m, s = [int(x) for x in time[j - 1].split(':')]
                team[j] = team[j] + m * 60 + s

        res = sorted(team.items(), key=lambda a: a[1])

        for k, v in res:
            print(k, v)
    except EOFError:
        break
