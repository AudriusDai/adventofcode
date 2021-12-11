class Vector:
    x_1: int
    y_1: int
    x_2: int
    y_2: int

    def __init__(self, x_1: int, y_1: int, x_2: int, y_2: int):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2

    def is_vertical(self):
        return self.x_1 == self.x_2

    def is_horizontal(self):
        return self.y_1 == self.y_2

    def is_diagonal(self):
        return not (self.is_vertical() or self.is_horizontal())
