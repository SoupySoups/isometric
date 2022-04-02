def isometric(x, y, z):
    return x * 10 - y * 10, x * 5 + y * 5 - z * 14


def rev_isometric(isometricx, isometricy, z):
    y = (isometricy / 5 - isometricx / 10 + z * 14 / 5) / 2
    return isometricx / 10 + y, y, z
