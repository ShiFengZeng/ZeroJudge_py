import sys

for y in sys.stdin:
    y = int(y)
    if y < 0:
        y += 109
    y = y % 12

    if y == 0:
        print("豬")
    elif y == 1:
        print("鼠")
    elif y == 2:
        print("牛")
    elif y == 3:
        print("虎")
    elif y == 4:
        print("兔")
    elif y == 5:
        print("龍")
    elif y == 6:
        print("蛇")
    elif y == 7:
        print("馬")
    elif y == 8:
        print("羊")
    elif y == 9:
        print("猴")
    elif y == 10:
        print("雞")
    else:
        print("狗")