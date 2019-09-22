for_mom = 0
remaining = 0
isLiability = False

for i in range(1, 13):
    expenditure = int(input())
    remaining = 300 - expenditure + remaining

    while remaining - 100 >= 0:
        for_mom += 100
        remaining -= 100

    if remaining < 0:
        print(-i)
        isLiability = True
        break

if not isLiability:
    print(remaining + int(for_mom * 1.2))
