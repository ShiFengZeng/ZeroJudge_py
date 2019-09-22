def cal(number, p):
    res = 0
    while number > 0:
        res += (number % 10) ** p
        number //= 10
    return res


n = int(input())
nums = [int(x) for x in input().split()]
nums_copy = nums.copy()

for i in range(2, 2 + n):
    for x in nums:
        num = cal(x, i)
        if num in nums_copy:
            nums_copy.remove(num)
        nums = nums_copy
nums.sort()
print(*nums)
