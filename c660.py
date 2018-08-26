while True:
    try:
        a = input().lower()
        for i in range(len(a)):
            if a[i] == ' ':
                continue
            print(a[0:i] + a[i].upper() + a[i+1:])
    except EOFError:
        break
