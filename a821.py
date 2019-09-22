import sys
N, R = [int(x) for x in input().split()]
team_win = {}
team_lose = {}
for inp in sys.stdin:
    sp = inp.split()
    win, lose = sp[0], sp[1]

    if win in team_win:
        team_win[win] = team_win[win] + 1
    else:
        team_win[win] = 1

    if lose in team_lose:
        team_lose[lose] = team_lose[lose] + 1
    else:
        team_lose[lose] = 1

win_max = max(team_win.values())

win_eq = []
for v in team_win.items():
    if v[1] == win_max:
        win_eq.append(v[0])

Min = 999
isSol = False
if len(win_eq) == 1:
    print(*win_eq)
else:
    for w in win_eq:
        lose_min = team_lose.get(w)
        if lose_min is None:
            print(w)
            isSol = True
            break
        else:
            Min = min(Min, lose_min)
    if not isSol:
        for w in win_eq:
            if team_lose[w] == Min:
                print(w)