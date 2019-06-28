################## MatrixC ##################

import numpy as np
from GlobalData import specific_heat, density, N_POINTS_Q
import UniversalElement as ue


class MatrixC:
    def __init__(self, le):
        intBody = np.zeros((N_POINTS_Q, 4, 4))

        for i in range(N_POINTS_Q):
            for j in range(4):
                for k in range(4):
                    intBody[i][j][k] = ue.N.T[i][j] * ue.N.T[i][k]
            intBody[i] *= le.detJ[i] * ue.W.flatten()[i]

        intBody *= specific_heat * density
        intBody = np.array(intBody)

        MatrixC = np.zeros((4, 4))

        # for i in range(4):
        #     for j in range(4):
        for i in range(N_POINTS_Q):
            MatrixC += intBody[i]

        self.MatrixC = MatrixC.reshape((4, 4))

