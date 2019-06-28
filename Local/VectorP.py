
################## VectorP ##################

import numpy as np
from Data.GlobalData import alpha, ambient_temperature
from Data.UniversalElement import N_creator
import math

class VectorP:
    def __init__(self, le):
     
        VectorP = []

        for i in range(4):
            if le.edges[i] and le.edges[i + 1 if i +1 < 4 else 0]:
                VectorP.append(
                        np.multiply(le.N_bc[i].T[0], alpha * le.detJe[i] * ambient_temperature)
                        + np.multiply(le.N_bc[i].T[1], alpha * le.detJe[i] * ambient_temperature)
                )
        
        self.VectorP = np.sum(VectorP[i] for i in range(len(VectorP)))





