s = input()
print(s[0] + ''.join(['_' for x in range(len(s) - 2)]) + s[-1])
