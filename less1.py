class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        if isinstance(other, Rectangle):
            total = self.get_square() + other.get_square()
            new_width = self.width
            new_height = total /  new_width
            return Rectangle(new_width, new_height)

    def __mul__(self, n):
        return Rectangle(self.width * n, self.height * n)

    def __str__(self):
        return f"Rectangle: {self.width}, {self.height}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
r1.get_square()
r2.get_square()

r3 = r1 + r2
r3.get_square()

r4 = r1 * 4
r4.get_square()

Rectangle(3, 6)
