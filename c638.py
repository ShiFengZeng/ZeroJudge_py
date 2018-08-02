def get_fist(n):
    return ["庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁", "戊", "己"][n]


def get_last(n):
    return ["申", "酉", "戌", "亥", "子", "丑", "寅", "卯", "辰", "巳", "午", "未"][n]


while 1:
    try:
        year = int(input())
        print(get_fist(year % 10) + get_last(year % 12))
    except EOFError:
        break
