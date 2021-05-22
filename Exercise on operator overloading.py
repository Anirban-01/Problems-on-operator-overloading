# As an exercise , add a method __sub__(self, other) that overloads the subtraction operator, and try it out.
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y


p = Point()
p1 = Point(2, 4)
p2 = Point(4, 6)

print(p1-p2)
