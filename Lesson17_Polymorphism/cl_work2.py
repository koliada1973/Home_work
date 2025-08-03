import turtle as t

class Shape:
    def __init__(self, x, y, radius, n):
        self.x = x
        self.y = y
        self.n = n
        self.radius = radius

    def DrawShape(self):
        raise NotImplementedError

class SquareShape(Shape):
    def DrawShape(self):
        t.setx(self.x)
        t.sety(self.y)
        t.down
        for i in range(self.n):
            t.forward(self.radius)
            t.right(360/self.n)
        t.up

my_shape = SquareShape(0, 0, 25, 10)
my_shape.DrawShape()
t.done