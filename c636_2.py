import sys

Zodiac = ['豬', "鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗"]
for y in sys.stdin:
    y = int(y)
    if y < 0:
        y += 109
    print(Zodiac[y % 12])