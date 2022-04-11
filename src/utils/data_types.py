class Point:
    def __init__(self, x, y, z=None) -> None:
        if z is not None:
            self.x, self.y, self.z = Point3D(x, y, z).as_tuple()
            self.type = Point3D
            self.two_d = False
        else:
            self.x, self.y = Point2D(x, y).as_tuple()
            self.type = Point2D
            self.two_d = True

    def __str__(self) -> str:
        return f'Point at {self.x}, {self.y}{f", {self.z}" if not self.two_d else ""}'

    def __repr__(self) -> str:
        return f'{self.x}, {self.y}{f", {self.z}" if not self.two_d else ""}'

    def check_3d(self) -> bool:
        if self.type != Point3D:
            raise TypeError("Point must be 3D")
        return True

    def check_2d(self) -> bool:
        if self.type != Point2D:
            raise TypeError("Point must be 2D")
        return True

    def as_tuple(self) -> tuple:
        return (self.x, self.y, self.z) if self.type != Point2D else (self.x, self.y)


class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        self.type = self

    def __str__(self) -> str:
        return f"Point2D at {self.x}, {self.y}"

    def __repr__(self) -> str:
        return f"{self.x}, {self.y}"

    def as_tuple(self) -> tuple:
        return (self.x, self.y)

    def check_3d(self) -> bool:
        return False

    def check_2d(self) -> bool:
        return True


class Point3D:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

        self.type = self

    def __str__(self) -> str:
        return f"Point3D at {self.x}, {self.y}, {self.z}"

    def __repr__(self) -> str:
        return f"{self.x}, {self.y}, {self.z}"

    def as_tuple(self) -> tuple:
        return (self.x, self.y, self.z)

    def check_3d(self) -> bool:
        return True

    def check_2d(self) -> bool:
        return False
