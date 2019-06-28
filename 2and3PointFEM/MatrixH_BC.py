################## MatrixH_BC ##################

import numpy as np
from GlobalData import alpha, N_POINTS
from UniversalElement import N_bc, w
import math


class MatrixH_BC:
    def __init__(self, le):

        detJe = []  # = 0.0125
        for i in range(4):
            detJe.append(
                np.linalg.norm(
                    np.array(le.coords)[i + 1 if i + 1 < 4 else 0]
                    - np.array(le.coords)[i]
                )
                / 2
            )

        def integralPoint(arr1, alpha):
            arr = np.zeros((4, 4))
            for i in range(4):
                for j in range(4):
                    arr[i][j] = arr1[i] * arr1[j] * alpha
            return arr

        intBody = []

        for i in range(4):
            if le.edges[i] and le.edges[i + 1 if i + 1 < 4 else 0]:
                arrSum = np.zeros((4, 4))
                for j in range(N_POINTS):
                    arrSum += integralPoint(N_bc[i, :, j], alpha) * w[j]
                intBody.append(np.multiply(arrSum, detJe[i]))

        MatrixH_BC = np.zeros((4, 4))

        for i in range(len(intBody)):
            MatrixH_BC += intBody[i]

        self.detJe = detJe
        self.MatrixH_BC = MatrixH_BC
