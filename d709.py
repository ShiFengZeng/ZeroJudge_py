from math import sqrt

isPrime = list(map(lambda i: True if i >= 2 else False, range(0, 1000001)))

for a in range(2, int(sqrt(1000000))):
    if isPrime[a]:
        b = a * a
        while b <= 1000000:
            isPrime[b] = False
            b += a

result = ''
while True:
    n = int(input())
    if n != 0:
        if isPrime[n]:
            result += '0\n'
        else:
            result += '1\n'
    else:
        print(result)
        break
