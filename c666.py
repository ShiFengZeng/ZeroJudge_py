from math import sqrt

isPrime = list(map(lambda i: True if i >= 2 else False, range(0, 48612)))
primes = []

for a in range(2, int(sqrt(48611))):
    if isPrime[a]:
        b = a * a
        while b <= 48611:
            isPrime[b] = False
            b += a
for m in range(2, 48612):
    if isPrime[m]:
        primes.append(m)

mulPrime = [0 for i in range(5001)]
mulPrime[1] = primes[0]
mulPrime[2] = primes[1] * primes[0]
for i in range(3, 5001):
    mulPrime[i] = mulPrime[i - 1] * primes[i-1]

while True:
    try:
        line = int(input())
        print(mulPrime[line])
    except EOFError:
        break
