import numpy as np
import math
from GlobalData import N_POINTS

xiPos = [-1, 1, 1, -1]
etaPos = [-1, -1, 1, 1]


def localCoordinates(points: int):
    if points == 2:
        return np.array(xiPos) * 1 / math.sqrt(3), np.array(etaPos) * 1 / math.sqrt(3)
    else:
        return [
            -math.sqrt(3 / 5),
            0,
            math.sqrt(3 / 5),
            -math.sqrt(3 / 5),
            0,
            math.sqrt(3 / 5),
            -math.sqrt(3 / 5),
            0,
            math.sqrt(3 / 5),
        ],[
            -math.sqrt(3 / 5),
            -math.sqrt(3 / 5),
            -math.sqrt(3 / 5),
            0,
            0,
            0,
            math.sqrt(3 / 5),
            math.sqrt(3 / 5),
            math.sqrt(3 / 5),
        ]


def weights(points: int):
    if points == 2:
        w = [1, 1]
    else:
        w = np.array([5/9, 8/9, 5/9])
    return w, np.array([[w[i] * w[j] for i in range(points)] for j in range(points)])


xi, eta = localCoordinates(N_POINTS)
w, W = weights(N_POINTS)

"""
N1 = 1/4 * (1 - xi) * (1 - eta)
N2 = 1/4 * (1 + xi) * (1 - eta)
N3 = 1/4 * (1 + xi) * (1 + eta)
N4 = 1/4 * (1 - xi) * (1 + eta)
"""


def N_creator(xi, eta):
    return np.array(
        (
            1 / 4 * np.subtract(1, xi) * np.subtract(1, eta),  # N1
            1 / 4 * np.add(1, xi) * np.subtract(1, eta),  # N2
            1 / 4 * np.add(1, xi) * np.add(1, eta),  # N3
            1 / 4 * np.subtract(1, xi) * np.add(1, eta),  # N4
        )
    )


N = N_creator(xi, eta)

dN_dXi = np.array(
    (
        np.dot(-1, np.subtract(1, eta) / 4),  # N1
        np.dot(1, np.subtract(1, eta) / 4),  # N2
        np.dot(1, np.add(1, eta) / 4),  # N3
        np.dot(-1, np.add(1, eta) / 4),  # N4
    )
)

dN_dEta = np.array(
    (
        np.dot(-1, np.subtract(1, xi) / 4),  # N1
        np.dot(-1, np.add(1, xi) / 4),  # N2
        np.dot(1, np.add(1, xi) / 4),  # N3
        np.dot(1, np.subtract(1, xi) / 4),  # N4
    )
)

N_bc = np.array(
    [
        N_creator([-1 / math.sqrt(3), 1 / math.sqrt(3)], [-1, -1]),
        N_creator([1, 1], [-1 / math.sqrt(3), 1 / math.sqrt(3)]),
        N_creator([1 / math.sqrt(3), -1 / math.sqrt(3)], [1, 1]),
        N_creator([-1, -1], [1 / math.sqrt(3), -1 / math.sqrt(3)]),
    ]
) if N_POINTS == 2 else np.array(
    [
        N_creator([-math.sqrt(3/5), 0, math.sqrt(3/5)], [-1, -1, -1]),
        N_creator([1, 1, 1], [-math.sqrt(3/5), 0, math.sqrt(3/5)]),
        N_creator([-math.sqrt(3/5), 0, math.sqrt(3/5)], [1, 1, 1]),
        N_creator([-1, -1, -1], [-math.sqrt(3/5), 0, math.sqrt(3/5)]),
    ]
)
