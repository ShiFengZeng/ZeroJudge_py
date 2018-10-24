from math import gcd

N = int(input())
for _ in range(N):
    nums = [int(x) for x in input().split()]
    Max = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            Max = max(Max, gcd(nums[i], nums[j]))
    print(Max)
