import math


tps = 30
d = 3
r = 2


def find_angles_triangles():
    pass


def find_angles_circles(u: float, v: float) -> list[tuple[float, float]]:
    h = ((r**2) - (d**2) - (u**2) - (v**2)) / 2
    z = (u*d)**2 - h**2 + (v*d)**2

    if z < 0:
        theta = math.degrees(math.acos(u / (u**2 + v**2)))
        return [(theta, theta)]

    k = h / v

    x1 = (-u*h + v*math.sqrt(z)) / (u**2 + v**2)
    x2 = (-u*h - v*math.sqrt(z)) / (u**2 + v**2)

    y1 = -(u/v) * x1 - k
    y2 = -(u/v) * x2 - k

    alpha1 = math.degrees(math.atan(y1 / x1))
    alpha2 = math.degrees(math.atan(y2 / x2))

    beta1 = math.degrees(math.acos((u - x1) / r))
    beta2 = math.degrees(math.acos((u - x2) / r))

    return [(alpha1, beta1), (alpha2, beta2)]

