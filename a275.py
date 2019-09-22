while True:
    a = input()
    if a == 'STOP!!':
        break
    b = input()
    asc = [0] * 127

    for i in a:
        asc[ord(i)] += 1
    for j in b:
        asc[ord(j)] -= 1

    is_OK = True
    for k in asc:
        if k != 0:            
            is_OK = False
            break
    if is_OK:
        print('yes')
    else:
        print('no')