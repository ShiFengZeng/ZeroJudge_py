n = int(input()) + 1
ans = []
for i in range(1, n):
    ans.append(f"{i}. I don't say swear words!")
print(str.join('\n', ans))
