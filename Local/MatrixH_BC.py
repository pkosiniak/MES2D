################## MatrixH_BC ##################

import numpy as np
from Data.GlobalData import alpha
from Data.UniversalElement import N_creator
import math


class MatrixH_BC:
    def __init__(self, le):

        self.N_bc = np.array(
            [
                N_creator([-1 / math.sqrt(3), 1 / math.sqrt(3)], [-1, -1]),
                N_creator([1, 1], [-1 / math.sqrt(3), 1 / math.sqrt(3)]),
                N_creator([1 / math.sqrt(3), -1 / math.sqrt(3)], [1, 1]),
                N_creator([-1, -1], [1 / math.sqrt(3), -1 / math.sqrt(3)]),
            ]
        )

        self.detJe = []  # = 0.0125
        for i in range(4):
            self.detJe.append(
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

        # print("\ndetJe\n")
        # print(self.detJe)

        arrSum = []
        for i in range(4):
            if le.edges[i] and le.edges[i + 1 if i + 1 < 4 else 0]:
                arrSum.append(
                    np.multiply(
                        integralPoint(self.N_bc[i].T[0], alpha)
                        + integralPoint(self.N_bc[i].T[1], alpha),
                        self.detJe[i],
                    )
                )

        arrSum = np.array(arrSum).flatten()

        arrSumFlat = np.zeros(4 * 4 * 4)
        arrSumFlat[0 : len(arrSum)] = arrSum

        MatrixH_BC = np.zeros(4 * 4)

        for i in range(4 * 4):
            MatrixH_BC[i] = np.sum(arrSumFlat[[i + 4 * 4 * k for k in range(4)]])

        self.MatrixH_BC = MatrixH_BC.reshape((4, 4))

