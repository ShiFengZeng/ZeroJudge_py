uglyName = [0] * 1501
uglyName[1] = 1
n2 = n3 = n5 = 1

for i in range(2, 1501):
    while uglyName[n2] * 2 <= uglyName[i - 1]:
        n2 += 1
    while uglyName[n3] * 3 <= uglyName[i - 1]:
        n3 += 1
    while uglyName[n5] * 5 <= uglyName[i - 1]:
        n5 += 1

    uglyName[i] = min(uglyName[n2]*2, uglyName[n3]*3, uglyName[n5]*5)

print("The 1500'th ugly number is {}.".format(uglyName[1500]))