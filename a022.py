while True:
    try:
        isPalindromes = True
        s = input()
        for i in range(int(len(s) / 2)):
            if s[i] != s[-1 - i]:
                isPalindromes = False
                break

        if isPalindromes:
            print('yes')
        else:
            print('no')
    except EOFError:
        break
