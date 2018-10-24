n = int(input())
up = [1] * (n + 1)
left = [1] * (n + 1)
right = [1] * (n + 1)

for i in range(2, n + 1):
    up[i] = up[i - 1] + left[i - 1] + right[i - 1]
    left[i] = left[i - 1] + up[i - 1]
    right[i] = right[i - 1] + up[i - 1]

print((up[n] + left[n] + right[n]) % 12345)
