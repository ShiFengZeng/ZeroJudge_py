M = input()
B = input()
T = int(input())
lenM = len(M)
lenB = len(B)
LCS = [[0 for i in range(lenB + 1)] for j in range(lenM + 1)]
for i in range(1, lenM + 1):
    for j in range(1, lenB + 1):
        if M[i - 1] == B[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

if LCS[lenM][lenB] >= T:
    print('kwa nini unaendesha')
else:
    print('sitini na tisa')
