class Point:
    def __init__(self, x, y, z=None) -> None:
        if z:
            self.x, self.y, self.z = Point3D(x, y, z).as_tuple()
            self.type = Point3D
        else:
            self.x, self.y = Point3D(x, y).as_tuple()
            self.type = Point3D
        
    def __str__(self) -> str:
        return f'Point at {self.x}, {self.y}{f", {self.z}" if not self.two_d else ""}'

    def __repr__(self) -> str:
        return f'{self.x}, {self.y}{f", {self.z}" if not self.two_d else ""}'

    def check_3d(self) -> bool:
        if not isinstance(self, Point3D):
            raise TypeError("Point must be 3D")
        return True

    def check_2d(self) -> bool:
        if not isinstance(self, Point2D):
            raise TypeError("Point must be 2D")
        return True

class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'Point2D at {self.x}, {self.y}'

    def __repr__(self) -> str:
        return f'{self.x}, {self.y}'

    def as_tuple(self) -> tuple:
        return (self.x, self.y)

class Point3D:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'Point3D at {self.x}, {self.y}, {self.z}'

    def __repr__(self) -> str:
        return f'{self.x}, {self.y}, {self.z}'

    def as_tuple(self) -> tuple:
        return (self.x, self.y, self.z)
        
        