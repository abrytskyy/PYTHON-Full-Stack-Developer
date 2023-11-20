#1. Declare three classes for geometric shapes: Line, Rect, Ellipse. It should be possible to create objects for
# each class with the following commands:
#
# g1 = Line(a, b, c, d)
# g2 = Rect(a, b, c, d)
# g3 = Ellipse(a, b, c, d)
# Here, the arguments a, b, c, d represent the coordinates of the upper right and lower left
# corners (arbitrary numbers). In each object, the coordinates should be stored in local properties sp
# (upper right corner) and ep (lower left) as tuples (a, b) and (c, d), respectively.
#
# Create 217 objects of these classes: for each current object, the class is randomly chosen
# (either Line, Rect, or Ellipse). Coordinates are also randomly generated (numeric values). Save all objects in the
# list elements.
#
# Set the coordinates to zero for objects only of the Line class in the elements list.

#solution 1-2 without __str__
import random

class Line:
    def __init__(self, a, b, c, d):
        self.spl = (a, b)
        self.epl = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.spr = (a, b)
        self.epr = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.spe = (a, b)
        self.epe = (c, d)

elements = []
for _ in range(217):
    class_shape = random.choice([Line, Rect, Ellipse])
    if class_shape == Line:
        element = class_shape(0, 0, 0, 0)
    else:
        element = class_shape(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))


    elements.append(element.__dict__)
for el in elements:
    print(el)

#solution 1-2 with __str__
import random

class Line:
    def __init__(self, a, b, c, d):
        self.spl = (a, b)
        self.epl = (c, d)

    def __str__(self):
        return f"right up corner{self.spl}, left down corner{self.epl}"

class Rect:
    def __init__(self, a, b, c, d):
        self.spr = (a, b)
        self.epr = (c, d)

    def __str__(self):
        return f"right up corner{self.spr}, left down corner{self.epr}"

class Ellipse:
    def __init__(self, a, b, c, d):
        self.spe = (a, b)
        self.epe = (c, d)

    def __str__(self):
        return f"right up corner{self.spe}, left down corner{self.epe}"

elements = []
for _ in range(217):
    class_shape = random.choice([Line, Rect, Ellipse])
    element = class_shape(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
    if class_shape == Line:
        element.spl = (0, 0)
        element.epl = (0, 0)

    elements.append(element)
for el in elements:
    print(el)




#2. Declare the class TriangleChecker, objects of which can be created with the command:
#
# tr = TriangleChecker(a, b, c)
# Here, a, b, c are the lengths of the sides of the triangle.
#
# In the TriangleChecker class, declare the method is_triangle(), which would return the following codes:
#
# 1 - if at least one side is not a number (not float or int), or if at least one number is less than or equal to zero;
# 2 - the specified numbers a, b, c cannot be the lengths of the sides of a triangle;
# 3 - the sides a, b, c form a triangle.
#
# Check the parameters a, b, c exactly in this order.
#
# Read a line from the input stream containing three numbers separated by spaces with the command:
#
# a, b, c = map(int, input().split())
#Then, create an object tr of the TriangleChecker class and pass the read values a, b, c to it. Call the is_triangle()
# method from the tr object and print the result on the screen (the code it will return).

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(isinstance(side, (int, float)) for side in [self.a, self.b, self.c]) or any(
                side <= 0 for side in [self.a, self.b, self.c]):
            return 1
        elif self.a + self.b <= self.c or self.b + self.c <= self.a or self.c + self.a <= self.b:
            return 2
        else:
            return 3


a,b,c = map(int, input().split())
tr = TriangleChecker(a, b, c)
code = tr.is_triangle()
print(code)

