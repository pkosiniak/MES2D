
################## VectorP ##################

import numpy as np
from GlobalData import alpha, ambient_temperature
from UniversalElement import N_bc, w, N_POINTS
import math

class VectorP:
    def __init__(self, le):
        
        detJe = le.detJe
        VectorP = []

        for i in range(4):
            if le.edges[i] and le.edges[i + 1 if i + 1 < 4 else 0]:
                vecSum = np.zeros(4)
                for j in range(N_POINTS):
                    vecSum += N_bc[i, :, j] * w[j]
                VectorP.append(np.multiply(vecSum, alpha * ambient_temperature * detJe[i]))

        self.VectorP = np.sum(VectorP[i] for i in range(len(VectorP)))


