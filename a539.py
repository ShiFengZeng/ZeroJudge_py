while 1:
    try:
        n = int(input())
        nums = [int(x) for x in input().split()]
        count = 0

        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    count += 1

        print("Minimum exchange operations : {}".format(count))
    except EOFError:
        break
