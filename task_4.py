class Rectangle:
    __x = 100
    __y = 100
    __width = 100
    __height = 50
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
    def __str__(self):
        return "Прямоугольник с координатами (" + str(self.x) + "; " + str(self.x) + ") шириной " + str(self.width) + " и высотой " + str(self.height)
    def ploshad(self):
        return self.x * self.y
    def perimetr(self):
        return (self.x + self.y) + 2
    def getX(self):
        self.__printlog("Запрошенно свойства " + str(self.__x))
        return self.__x
    def setX(self, x):
        self.__printlog("Параметр свойства " + str(self.__x))
        self.__x = x
    def getY(self):
        self.__printlog("Запрошенно свойства " + str(self.__y))
        return self.__y
    def setY(self, y):
        self.__printlog("Параметр свойства " + str(self.__y))
        self.__y = y
    def getWidth(self):
        self.__printlog("Запрошенно свойства " + str(self.__width))
        return self.__width
    def setWidth(self, width):
        self.__printlog("Параметр свойства " + str(self.__width))
        self.__width = width
    def getHeight(self):
        self.__printlog("Запрошенно свойства " + str(self.__height))
        return self.__height
    def setHeight(self, height):
        self.__printlog("Параметр свойства " + str(self.__height))
        self.__height = height
    def __printlog(self, parmet):
        print(parmet)



pect = Rectangle(100, 100, 50, 50)
print(pect.getX())