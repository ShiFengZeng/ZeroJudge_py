import sys

Humble_Number = [0] * 5843
Humble_Number[1] = 1

n2 = n3 = n5 = n7 = 1

for i in range(2, 5843):
    while Humble_Number[n2] * 2 <= Humble_Number[i - 1]:
        n2 += 1
    while Humble_Number[n3] * 3 <= Humble_Number[i - 1]:
        n3 += 1
    while Humble_Number[n5] * 5 <= Humble_Number[i - 1]:
        n5 += 1
    while Humble_Number[n7] * 7 <= Humble_Number[i - 1]:
        n7 += 1

    Humble_Number[i] = min(Humble_Number[n2] * 2, Humble_Number[n3] * 3, Humble_Number[n5] * 5, Humble_Number[n7] * 7)

res = []
while True:
    n = int(sys.stdin.readline())

    if n == 0:
        print("".join(res), end="")
        break
    if n % 10 == 1 and n % 100 != 11:
        res.append('The {}st humble number is '.format(n))
    elif n % 10 == 2 and n % 100 != 12:
        res.append('The {}nd humble number is '.format(n))
    elif n % 10 == 3 and n % 100 != 13:
        res.append('The {}rd humble number is '.format(n))
    else:
        res.append('The {}th humble number is '.format(n))
    res.append(str(Humble_Number[n]) + '.\n')
