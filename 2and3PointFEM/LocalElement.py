import math
import numpy as np
from GlobalData import *
from UniversalElement import *
from Structures import Element, Node
from MatrixH import MatrixH
from MatrixC import MatrixC
from MatrixH_BC import MatrixH_BC
from VectorP import VectorP
from typing import List


class LocalElement:
    def __init__(self, element: Element):

        self.x = []  # [0, 0.025, 0.025, 0]
        self.y = []  # [0, 0, 0.025, 0.025]
        self.edges = []
        self.coords = []
        for node in element.nodes:
            self.x.append(node.x)
            self.y.append(node.y)
            self.coords.append([node.x, node.y])
            self.edges.append(node.isEdge)

        # foreach PC
        dx_dXi = np.array([np.multiply(dN_dXi[i], self.x[i])
                           for i in range(4)])
        self.dx_dXi = [np.sum(dx_dXi[:, i]) for i in range(N_POINTS_Q)]

        dx_dEta = np.array([np.multiply(dN_dEta[i], self.x[i])
                            for i in range(4)])
        self.dx_dEta = [np.sum(dx_dEta[:, i]) for i in range(N_POINTS_Q)]

        dy_dXi = np.array([np.multiply(dN_dXi[i], self.y[i])
                           for i in range(4)])
        self.dy_dXi = [np.sum(dy_dXi[:, i]) for i in range(N_POINTS_Q)]

        dy_dEta = np.array([np.multiply(dN_dEta[i], self.y[i])
                            for i in range(4)])
        self.dy_dEta = [np.sum(dy_dEta[:, i]) for i in range(N_POINTS_Q)]

        #Jacobian
        J = np.array(
            [
                [self.dx_dXi[i], self.dy_dXi[i], self.dx_dEta[i], self.dy_dEta[i]]
                for i in range(N_POINTS_Q)
            ]
        ).reshape((N_POINTS_Q, 2, 2))

        self.detJ = [np.linalg.det(J[i]) for i in range(N_POINTS_Q)]

        invJ = []

        for i in range(N_POINTS_Q):
            invJ.append([J[i][1][1], np.dot(-1, J[i][0][1]),
                         np.dot(-1, J[i][1][0]), J[i][0][0]])
            invJ[-1] = np.dot(1 / self.detJ[i], invJ[-1])

        self.invJ = np.array(invJ).reshape((N_POINTS_Q, 4))

        self.dN_dx = np.zeros((N_POINTS_Q, 4))
        self.dN_dy = np.zeros((N_POINTS_Q, 4))

        for j in range(4):
            for i in range(N_POINTS_Q):
                self.dN_dx[i][j] = (
                    self.invJ[i][0] * dN_dXi.T[i][j]
                    + self.invJ[i][1] * dN_dEta.T[i][j]
                )
                self.dN_dy[i][j] = (
                    self.invJ[i][2] * dN_dXi.T[i][j]
                    + self.invJ[i][3] * dN_dEta.T[i][j]
                )

    def CalcElements(self):
        self.MatrixH = MatrixH(self).MatrixH
        self.MatrixC = MatrixC(self).MatrixC
        mhbc = MatrixH_BC(self)
        self.MatrixH_BC = mhbc.MatrixH_BC
        self.detJe = mhbc.detJe
        self.MatrixH += self.MatrixH_BC
        # for i in range(4):
        #     for j in range(4):
        #         self.MatrixH[i][j] += self.MatrixH_BC[i][j]
        self.VectorP = VectorP(self).VectorP
        return self


# # print("\n\nW\n",W)
# le = LocalElement(
#     Element(
#         [
#             Node(1, 0., 0., 100, True),
#             Node(5, 0.025, 0., 100, True),
#             Node(6, 0.025, 0.025, 100, False),
#             Node(2, 0., 0.025, 100, True),
#         ]
#     )
# )
