import sys

level = ('Saber', 'Lancer', 'Archer',
         'Rider', 'Caster', 'Assassin', 'Berserker')
n = [0] * 7
for line in sys.stdin:
    for l in line:
        if str.isalpha(l):
            n[(ord(l.lower()) - ord('a')) % 7] += 1

max_count = max(n)
for i in range(7):
    if n[i] == max_count:
        print(level[i])
        break
