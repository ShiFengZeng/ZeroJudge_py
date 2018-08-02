def to_hex(s):
    out = ''
    out += str(int(s[1:3], 16)) + ' ' + str(int(s[3:5], 16)) + ' ' + str(int(s[5:7], 16))
    return out


def to_rgb(s):
    out = '#'
    tmp1 = hex(int(s.split()[0]))[2:]
    tmp2 = hex(int(s.split()[1]))[2:]
    tmp3 = hex(int(s.split()[2]))[2:]
    out += tmp1 if len(tmp1) == 2 else '0' + str(tmp1)
    out += tmp2 if len(tmp2) == 2 else '0' + str(tmp2)
    out += tmp3 if len(tmp3) == 2 else '0' + str(tmp3)
    return out


while 1:
    try:
        line = input()
        if line[0] == '#':
            print(to_hex(line))
        else:
            print(to_rgb(line).upper())
    except EOFError:
        break
