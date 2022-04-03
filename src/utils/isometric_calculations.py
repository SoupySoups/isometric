import src.utils.data_types as data_types


def isometric(point: data_types.Point3D):
    point.check_3d()
    return data_types.Point(
        point.x * 10 - point.y * 10, point.x * 5 + point.y * 5 - point.z * 14
    )


def rev_isometric(point: data_types.Point2D, z):
    point.check_2d()
    y = (point.y / 5 - point.x / 10 + z * 14 / 5) / 2
    return data_types.Point(point.x / 10 + y, y, z)
