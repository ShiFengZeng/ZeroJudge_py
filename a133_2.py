from sys import stdin

num = 1
LCS = [[0 for i in range(101)] for j in range(101)]
while True:
    N1, N2 = [int(x) for x in stdin.readline().split()]
    if N1 == N2 == 0:
        break
    else:

        tower1 = stdin.readline().split()  # tower1[]=
        tower2 = stdin.readline().split()  # tower2[]=

        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                if tower1[i - 1] == tower2[j - 1]:
                    LCS[i][j] = LCS[i - 1][j - 1] + 1
                else:
                    LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
        print('Twin Towers #%d' % num)
        print('Number of Tiles : %d' % LCS[N1][N2])
        num += 1
