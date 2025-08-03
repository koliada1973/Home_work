class C:
    def __init__(self):
        self._x = "HELLO"

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    our_property = property(getx, setx, delx, "I'm the 'x' property.")

c = C()
print(c.our_property)
c.our_property = 'Test'
print(c.our_property)