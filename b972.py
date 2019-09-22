while True:
    try:
        n, t = [int(x) for x in input().split()]
        team = [0] * t

        for i in range(n):
            time = input().split()
            for j in range(t):
                m, s = [int(x) for x in time[j].split(':')]
                team[j] += m * 60 + s

        team.sort()
        for i in range(t):
            print(team[i])
    except EOFError:
        break
