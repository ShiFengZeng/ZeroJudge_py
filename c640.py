import sys


def gcd(a, b):
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def gcd_arr(arrs):
    length = len(arrs)
    for i in range(length - 1):
        arrs[i + 1] = gcd(int(arrs[i]), int(arrs[i + 1]))
    return int(arrs[length - 1])


def lcm_arr(arrs):
    length = len(arrs)
    for i in range(length - 1):
        arrs[i + 1] = lcm(int(arrs[i]), int(arrs[i + 1]))
    return int(arrs[length - 1])


for inp in sys.stdin:
    M, k = inp.split()
    M = int(M)
    k = int(k)
    if __name__ == '__main__':
        inp = input()
        arr = []
        arr.extend(inp.split())
        i = 1

        lcms = lcm_arr(arr)
        while lcms * i + k <= M:
            print(lcms * i + k, end=' ')
            i += 1
        print()
