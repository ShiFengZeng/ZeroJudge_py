n = int(input())
nums = dict()
for _ in range(n):
    num = int(input())
    if num in nums:
        nums[num] = nums[num] + 1
    else:
        nums[num] = 1
res = sorted(nums.items(), key=lambda n: n[0])

for r in res:
    print(r[0], r[1])
