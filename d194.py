T = int(input())
for i in range(T):
    n = int(input())
    A = []
    for j in range(n):
        snowflake = int(input())
        A.append(snowflake)

    res = set()
    leftIndex = rightIndex = maxLen = 0
    while rightIndex < len(A):
        if not A[rightIndex] in res:
            res.add(A[rightIndex])
            rightIndex += 1
            maxLen = max(maxLen, rightIndex - leftIndex)
        else:
            res.remove(A[leftIndex])
            leftIndex += 1

    print(maxLen)
