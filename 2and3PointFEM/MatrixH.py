################## MatrixH ##################
import numpy as np
from GlobalData import conductivity, N_POINTS_Q
from UniversalElement import W




class MatrixH:
    def __init__(self, le):

        partX = np.zeros((N_POINTS_Q, 4, 4))
        partY = np.zeros((N_POINTS_Q, 4, 4))
        intBody = np.zeros((N_POINTS_Q, 4, 4))

        for i in range(N_POINTS_Q):
            for j in range(4):
                for k in range(4):
                    partX[i][j][k] = le.dN_dx[i][j] * le.dN_dx[i][k]
                    partY[i][j][k] = le.dN_dy[i][j] * le.dN_dy[i][k]
                    intBody[i][j][k] = partX[i][j][k] + partY[i][j][k]
            intBody[i] *= conductivity * le.detJ[i] * W.flatten()[i]

        intBody = np.array(intBody)

        MatrixH = np.zeros((4, 4))
        
        for k in range(N_POINTS_Q):
            MatrixH += intBody[k]

        # for i in range(4):
        #     for j in range(4):
                
        #             MatrixH[i, j] += intBody[k, i, j]

        self.MatrixH = MatrixH
