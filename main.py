class Vector:
    def __init__(self, *args):
        self.coords = args

    def valid_check_len(self, v2):
        if len(self.coords) != len(v2.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        return True

    def __add__(self, other):
        if isinstance(other, Vector) and self.valid_check_len(other):
            return Vector(*tuple(x1 + y1 for x1, y1 in zip(self.coords, other.coords)))

    def __iadd__(self, other):
        if type(other) in (int, float):
            self.coords = tuple(x1 + other for x1 in self.coords)
        if isinstance(other, Vector) and self.valid_check_len(other):
            self.coords = tuple(x1 + y1 for x1, y1 in zip(self.coords, other.coords))
        return self

    def __sub__(self, other):
        if isinstance(other, Vector) and self.valid_check_len(other):
            return Vector(*tuple(x1 - y1 for x1, y1 in zip(self.coords, other.coords)))

    def __isub__(self, other):
        if type(other) in (int, float):
            self.coords = tuple(x1 - other for x1 in self.coords)
        if isinstance(other, Vector) and self.valid_check_len(other):
            self.coords = tuple(x1 - y1 for x1, y1 in zip(self.coords, other.coords))
        return self

    def __mul__(self, other):
        if isinstance(other, Vector) and self.valid_check_len(other):
            return Vector(*tuple(x1 * y1 for x1, y1 in zip(self.coords, other.coords)))

    def __eq__(self, other):
        self.valid_check_len(other)
        return all(x1 == y1 for x1, y1 in zip(self.coords, other.coords))
