input()
w = [int(x) for x in input().split()]
c = 0
for i in w:
    if i <= 10:
        c += 1
print(c)
