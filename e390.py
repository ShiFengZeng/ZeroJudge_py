import binascii


def get_gig5_hex_string(source):
    return binascii.hexlify(source.encode("big5")).decode('ascii')


while 1:
    try:
        s = get_gig5_hex_string(input())
        if s.endswith('5c') and len(s) == 4:
            print('Yes')
        else:
            print('No')
    except EOFError:
        break
