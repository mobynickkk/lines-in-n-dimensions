class Tensor(list):
    @staticmethod
    def __is_number(x):
        return type(x) == int or type(x) == float

    def __init__(self, data):
        _data = list(data)
        self.depth = 1 if type(next(iter(_data))) != Tensor else next(iter(_data)).depth + 1
        tensor = [batch if self.__is_number(batch) else Tensor(batch) for batch in _data]
        super(Tensor, self).__init__(tensor)

    def __str__(self):
        inline = ', '
        break_line = ',\n '
        return f'({(inline if self.depth == 1 else break_line).join(map(str, self))})'

    @staticmethod
    def get_vector(x, y):
        return Tensor(map(lambda i: x[i] - y[i], range(len(x))))

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
        return Tensor(map(lambda i: self[i] + other[i], range(len(self))))

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Tensor(map(lambda i: self[i] * other, range(len(self))))
        elif type(other) == Tensor:
            return sum(self + other)

    def __neg__(self):
        return -1 * self

    def is_way_between(self, a, b) -> bool:
        try:
            count = (b[0] - a[0]) / self[0]
            return all(map(lambda i: b[i] == (a[i] + count * self[i]), range(len(self))))
        except ZeroDivisionError:
            return False

    def flatten(self):
        if self.depth == 1:
            return self
        from functools import reduce
        return Tensor(reduce(lambda a, x: a.append(x.flatten()), self, []))
