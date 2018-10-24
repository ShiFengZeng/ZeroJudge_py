from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(point1, point2):
    _x = point1.x - point2.x
    _y = point1.y - point2.y
    return sqrt(_x * _x + _y * _y)


while 1:
    try:
        x1, y1, x2, y2, x3, y3 = [float(x) for x in input().split()]
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        p3 = Point(x3, y3)

        a = distance(p1, p2)
        b = distance(p1, p3)
        c = distance(p2, p3)

        s = (a + b + c) / 2  # 海龍公式
        area = sqrt(s * (s - a) * (s - b) * (s - c))  # 海龍公式 面積
        r = a * b * c / (4 * area)  # 外接圓半徑 r=a*b*c/(4*area)
        PI = 3.141592653589793

        print("%.2f" % (2 * PI * r))
    except EOFError:
        break
