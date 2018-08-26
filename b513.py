from math import sqrt

isNotPrime = list(map(lambda i: True if i < 2 else False, range(0, 65536)))
primes = []

for a in range(2, int(sqrt(65535))):
    if not isNotPrime[a]:
        b = a * a
        while b <= 65535:
            isNotPrime[b] = True
            b += a
while True:
    try:
        n = int(input())
        while n:
            x = int(input())
            if not isNotPrime[x]:
                print('Y')
            else:
                print('N')

            n -= 1
    except EOFError:
        break
