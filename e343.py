def bmi(w, h):
    return w / (h * h)


def main():
    w = int(input())
    h = int(input())
    print(f'{bmi(w, h / 100):.1f}')


if __name__ == '__main__':
    main()
