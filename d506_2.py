n = bin(86495)[2:]
c = 1
Sum = 1
for i in range(len(n) - 1, -1, -1):
    if int(n[i]) == 1:
        Sum *= (7 ** c)
    c *= 2
print(Sum)
