def is_exact_square_number(num):
    if num ** (1 / 2) % 1 == 0:
        return True
    else:
        return False


while True:
    n = int(input())
    if n == 0:
        break
    if is_exact_square_number(n):
        print('yes')
    else:
        print('no')
