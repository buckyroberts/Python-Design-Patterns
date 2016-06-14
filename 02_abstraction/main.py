class Rectangle(object):

    @staticmethod
    def calculate_area(width, height):
        return width * height


# User does not need to know formula to get area of Rectangle
area = Rectangle.calculate_area(5, 7)
print(area)
