def leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def huluculu_year(y):
    if y % 15 == 0:
        return True
    else:
        return False


def bulukulu_year(y):
    if leap_year(y) and y % 55 == 0:
        return True
    else:
        return False


while True:
    try:
        year = int(input())
        ordinary = True

        if leap_year(year):
            ordinary = False
            print('This is leap year.')
        if huluculu_year(year):
            ordinary = False
            print('This is huluculu festival year.')
        if bulukulu_year(year):
            ordinary = False
            print('This is bulukulu festival year.')

        if ordinary:
            print('This is an ordinary year.')
        print()
    except EOFError:
        break
