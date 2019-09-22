m, n = [int(x) for x in input().split()]
team = dict()
for i in range(1, n + 1):
    team[i] = 0

Max = 0
for _ in range(m):
    inp = input().split()

    ans = inp[0]
    team_ans = inp[1:]

    team_no = team_ans[0::2]
    team_no_ans = team_ans[1::2]

    for i in range(len(team_no)):
        if team_no_ans[i] == ans:
            team[int(team_no[i])] = team[int(team_no[i])] + 1
            if team[int(team_no[i])] > Max:
                Max = team[int(team_no[i])]
            break

i = 1
while i < n + 1:
    if team[i] == Max:
        print(i, end="")
        i += 1
        break
    i += 1
while i < n + 1:
    if team[i] == Max:
        print(" ", end="")
        print(i, end="")
    i += 1
print()
for k, v in team.items():
    print(k, v)
