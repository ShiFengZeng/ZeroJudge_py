n = int(input())

cattle = [int(x) for x in input().split()]
cattle.sort()
num = 0

for i in range(int(n / 2)):
    num = max(num, cattle[i] + cattle[-1 - i])
print(num)
