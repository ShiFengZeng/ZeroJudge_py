def cal(a, b, c):
    return a * 0.2 + b * 0.3 + c * 0.5


def main():
    a, b, c = [int(x) for x in input().split()]
    print(int(cal(a, b, c)))


if __name__ == '__main__':
    main()
