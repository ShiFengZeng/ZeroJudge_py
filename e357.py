def F(num):
    if num == 1:
        return 1
    elif num & 1 == 0:
        return F(num // 2)
    else:
        return F(num - 1) + F(num + 1)


def main():
    number = int(input())
    print(F(number))


if __name__ == '__main__':
    main()
