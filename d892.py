M, N = [int(x) for x in input().split()]
words = [int(x) for x in input().split()]

machine = []
count = 0

for word in words:
    if word not in machine:
        if len(machine) < M:
            machine.append(word)
            count += 1
        else:
            machine.pop(0)
            machine.append(word)
            count += 1
print(count)
