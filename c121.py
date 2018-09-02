F = [0] * 5001
F[0] = 0
F[1] = 1
for i in range(2, 5001):
    F[i] = F[i - 1] + F[i - 2]
while True:
    try:
        n = int(input())
        print('The Fibonacci number for {0} is {1}'.format(n, F[n]))
    except EOFError:
        break
