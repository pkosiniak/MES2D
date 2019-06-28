################## MatrixC ##################

import numpy as np
from Data.GlobalData import specific_heat, density
import Data.UniversalElement as ue


class MatrixC:
    def __init__(self, le):
        intBody = np.zeros((4, 4, 4))

        for i in range(4):
            for j in range(4):
                for k in range(4):
                    intBody[i][j][k] = ue.N[i][j] * ue.N[i][k]
            intBody[i] *= le.detJ[i]

        intBody *= specific_heat * density
        intBody = intBody.flatten()
        MatrixC = np.zeros(4 * 4)

        for i in range(4 * 4):
            MatrixC[i] = np.sum(intBody[[i + 4 * 4 * k for k in range(4)]])

        self.MatrixC = MatrixC.reshape((4, 4))

