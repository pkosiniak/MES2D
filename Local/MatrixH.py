################## MatrixH ##################
import numpy as np
from Data.GlobalData import conductivity

class MatrixH:
	def __init__(self, le):

		partX = np.zeros((4, 4, 4))
		partY = np.zeros((4, 4, 4))
		intBody = np.zeros((4, 4, 4))

		for i in range(4):
			for j in range(4):
				for k in range(4):
						partX[i][j][k] = le.dN_dx[i][j] * le.dN_dx[i][k]
						partY[i][j][k] = le.dN_dy[i][j] * le.dN_dy[i][k]
						intBody[i][j][k] = partX[i][j][k] + partY[i][j][k]
			intBody[i] *= conductivity * le.detJ[i]

		intBody = intBody.flatten()
		MatrixH = np.zeros(4 * 4)

		for i in range(4 * 4):
			MatrixH[i] = np.sum(intBody[[i + 4 * 4 * k for k in range(4)]])
		self.MatrixH = MatrixH.reshape((4, 4))
	


