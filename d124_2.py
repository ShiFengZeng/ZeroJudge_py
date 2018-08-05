while True:
    try:
        a = int(input())
        print('yes' if a % 3 == 0 else 'no')
    except EOFError:
        break
