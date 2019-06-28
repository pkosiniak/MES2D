import numpy as np
import math

xiPos = [-1, 1, 1, -1]
etaPos = [-1, -1, 1, 1]

"""
#           PC1               PC2               PC3                PC4
xi = [-1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3), -1 / math.sqrt(3)]
eta = [-1 / math.sqrt(3), -1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3)]
"""

xi = np.array(xiPos) * 1 / math.sqrt(3)
eta = np.array(etaPos) * 1 / math.sqrt(3)


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

dN_dXi = (
    np.array(
        (
            np.subtract(1, eta) / 4,  # N1
            np.subtract(1, eta) / 4,  # N2
            np.add(1, eta) / 4,  # N3
            np.add(1, eta) / 4,  # N4
        )
    )
    * xiPos
)

dN_dEta = (
    np.array(
        (
            np.subtract(1, xi) / 4,  # N1
            np.add(1, xi) / 4,  # N2
            np.add(1, xi) / 4,  # N3
            np.subtract(1, xi) / 4,  # N4
        )
    )
    * etaPos
)
