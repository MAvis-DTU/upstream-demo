
class Foo:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"Foo[x={self.x}]"

    def increment(self):
        self.x += 1

