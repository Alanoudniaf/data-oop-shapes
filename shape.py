# pylint: disable=too-few-public-methods missing-module-docstring
import math

class Shape:
    """Base class for different shapes."""
    def __init__(self, color, name):
        """Initializes the shape with a color and name."""
        self.color = color
        self.name = name

    def say_name(self):
        """Returns the name of the shape."""
        return f"My name is {self.name}."

class Rectangle(Shape):
    """Class representing a rectangle."""
    def __init__(self, color, name, width, height):
        """Initializes the rectangle with color, name, width, and height."""
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):
        """Returns the name of the rectangle along with its shape type."""
        return f"My name is {self.name} and I am a rectangle."

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Class representing a circle."""
    def __init__(self, color, name, radius):
        """Initializes the circle with color, name, and radius."""
        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        """Returns the name of the circle along with its shape type."""
        return f"My name is {self.name} and I am a circle."

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculates and returns the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

# Testing
rect = Rectangle("Blue", "Rei", 5, 10)
circle = Circle("Red", "Kvothe", 7)

print(rect.say_name())
print(f"Rectangle Area: {rect.area()}")
print(f"Rectangle Perimeter: {rect.perimeter()}")

print(circle.say_name())
print(f"Circle Area: {circle.area():.2f}")
print(f"Circle Perimeter: {circle.perimeter():.2f}")
