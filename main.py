import math
class Otrezok:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2


    def get_Point1(self):
        return (self.__x1, self.__y1)

    def set_Point1(self, value):
        x12, y12 = value
        a = math.atan2((y12 - self.__y2), (x12 - self.__x2))
        L = math.sqrt((x12 - self.__x2)**2 + (y12 - self.__y2)**2)

        self.__x1 = x12
        self.__y1 = y12
        self.__x2 = L * math.cos(a) + x12
        self.__y2 = L * math.sin(a) + y12

    def get_Point2(self):
        return (self.__x2, self.__y2)

    def set_Point2(self, value):
        x22, y22 = value
        a = math.atan2((y22 - self.__y1), (x22 - self.__x1))
        L = math.sqrt((x22 - self.__x1)**2 + (y22 - self.__y1)**2)

        self.__x2 = x22
        self.__y2 = y22
        self.__x1 = L * math.cos(a) + x22
        self.__y1 = L * math.sin(a) + y22

otrezok1 = Otrezok(0, 0, 3, 4)
print("Исходные координаты отрезка 1:", otrezok1.get_Point1(), otrezok1.get_Point2())

otrezok2 = Otrezok(5, 5, 8, 1)
print("Исходные координаты отрезка 2:", otrezok2.get_Point1(), otrezok2.get_Point2())

