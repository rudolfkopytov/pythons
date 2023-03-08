class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.height = heigth

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # Метод, рассчитывающий площадь
    def get_area(self):
        return self.width * self.height
from rectangle import Rectangle

r1 = Rectangle(10, 5)

print("r1.width =", r1.width)
print("r1.height =", r1.height)
print("r1.get_width =", r1.get_width())
print("r1.get_height =", r1.get_height())
print("r1.get_area =", r1.get_area())