from functools import reduce

res = []
append = res.append
ans = str(reduce(lambda x, y: x * y, [j for i in range(1, 101) for j in range(2, i + 1)]))
for i in ans:
    append(i + "\n")
print("".join(res), end='')
