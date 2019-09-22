n = int(input())
for _ in range(n):
    AB_SET = input().split('}')
    A_SET = eval(AB_SET[0] + '}')
    B_SET = eval(AB_SET[1].strip(',') + '}')

    print(A_SET | B_SET, end="")

    A = A_SET & B_SET
    if A == set():
        A = 'N'
    else:
        A = sorted(A)
        A = "".join(str(A)).replace('[', '{').replace(']', '}')

    B = A_SET - B_SET
    if B == set():
        B = 'N'
    else:
        B = sorted(B)
        B = "".join(str(B)).replace('[', '{').replace(']', '}')

    C = A_SET ^ B_SET
    if C == set():
        C = 'N'
    else:
        C = sorted(C)
        C = "".join(str(C)).replace('[', '{').replace(']', '}')
    print(',', A, end="")
    print(',', B, end="")
    print(',', C, end="")
    print()
