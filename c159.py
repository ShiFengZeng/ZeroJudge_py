n = int(input())
isAdd = [False] * 20000
nums = [int(x) for x in input().split()]

for i in range(n - 1):
    for j in range(i + 1, n):
        isAdd[nums[i] + nums[j]] = True

count = 0
for i in range(n):
    if isAdd[nums[i]]:
        count += 1

print(count)
