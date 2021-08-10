class Vector(list):
    def __str__(self):
        return f'({",".join(map(str, self))})'

    @staticmethod
    def get_vector(x, y):
        return Vector(map(lambda i: x[i] - y[i], range(len(x))))

    @staticmethod
    def are_collinear(x, y) -> bool:
        try:
            c = x[0] / y[0]
            return all(map(lambda i: (x[i] / y[i]) == c, range(len(x))))
        except ZeroDivisionError:
            return False

    @staticmethod
    def get_linear_reducer(base):
        get_linear_coordinate = lambda vector: vector / base
        return lambda *args: map(get_linear_coordinate, args)

    def __truediv__(self, other):
        if self.are_collinear(self, other):
            return self[0] / other[0]

    def __add__(self, other):
        return Vector(map(lambda i: self[i] + other[i], range(len(self))))

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector(map(lambda i: self[i] * other, range(len(self))))
        elif type(other) == Vector:
            return sum(self + other)

    def __neg__(self):
        return -1 * self

    def is_way_between(self, a, b) -> bool:
        try:
            count = (b[0] - a[0]) / self[0]
            return all(map(lambda i: b[i] == (a[i] + count * self[i]), range(len(self))))
        except ZeroDivisionError:
            return False


def get_codirectional(x: Vector, y: Vector):
    if Vector.are_collinear(x, y):
        c = x[0] / y[0]
        return (-x, -y) if c < 0 else (x, y)
    return x, y
