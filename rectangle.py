
class Rectangle:
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color
    
    def calculate_area(self):
        self.area = self.length*self.width

        return self.area



rectangle = Rectangle(5, 3)
print(rectangle.length)


area = rectangle.calculate_area()
print(area)