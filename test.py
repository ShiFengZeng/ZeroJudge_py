

line = input()
row, col = [int(x) for x in line.split()]
# row, col = [int(x) for x in input().split()]
a = [[0 for i in range(col)] for j in range(row)]
print(a)