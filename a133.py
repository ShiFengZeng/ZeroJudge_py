num = 1

while True:
    N1, N2 = [int(x) for x in input().split()]
    if N1 == N2 == 0:
        break
    else:
        LCS = [[0 for i in range(N2 + 1)] for j in range(N1 + 1)]
        tower1 = input().split()  # tower1[]=
        tower2 = input().split()  # tower2[]=

        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                if tower1[i - 1] == tower2[j - 1]:
                    LCS[i][j] = LCS[i - 1][j - 1] + 1
                else:
                    LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
        print('Twin Towers #{0}'.format(num))
        print('Number of Tiles : {0}'.format(LCS[N1][N2]))
        num += 1
