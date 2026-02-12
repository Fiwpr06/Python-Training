# Extended Built-in Types
class MyList(list):
    def sum(self):
        """Return the sum of all elements in the list."""
        return sum(self)

    def average(self):
        """Return the average of all elements in the list."""
        if len(self) == 0:
            return 0
        return self.sum() / len(self)

    def max_value(self):
        """Return the maximum value in the list. If the list is empty, return None."""
        if len(self) == 0:
            return None
        return max(self)

    def min_value(self):
        """Return the minimum value in the list. If the list is empty, return None."""
        if len(self) == 0:
            return None
        return min(self)
    
    def __getitem__(self, index):
        """Return the element at the given index, but with 1-based indexing."""
        return list.__getitem__(self, index - 1)

# Example usage
L = MyList([10, 20, 30, 40, 50])
print("Sum:", L.sum())
print("Average:", L.average())
print("Max Value:", L.max_value())
print("Min Value:", L.min_value())
print("Element at 3rd position:", L[3], end="\n\n")

# Slot
class Vector:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

v = Vector(1, 2)
print(f"Vector: ({v.x}, {v.y})", end="\n\n")

# Static and Class Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @staticmethod
    def multiply(a, b):
        """Return the product of a and b."""
        return a * b

    @classmethod
    def description(cls):
        """Return a description of the MathUtils class."""
        return f"{cls.__name__} provides utility methods for mathematical operations."

# Example usage
print("Addition:", MathUtils.add(5, 3))
print("Multiplication:", MathUtils.multiply(5, 3))
print(MathUtils.description(), end="\n\n")

# Super()
class Shape:
    def __init__(self, color):
        self.color = color
        
    def display_info(self):
        """Print shape information."""
        print(f"Shape Color: {self.color}")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        super().display_info()
        return self.width * self.height

# Example usage
rect = Rectangle("Red", 5, 10)
print("Area of Rectangle:", rect.area())