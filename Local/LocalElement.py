import math
import numpy as np
from Data.GlobalData import *
from Data.UniversalElement import *
from Data.Structures import Element, Node
from Local.MatrixH import MatrixH
from Local.MatrixC import MatrixC
from Local.MatrixH_BC import MatrixH_BC
from Local.VectorP import VectorP
from typing import List


class LocalElement:
    def __init__(self, element: Element):

        self.x = []  # [0, 0.025, 0.025, 0]
        self.y = []  # [0, 0, 0.025, 0.025]
        self.edges = []
        self.coords = []
        for node in element.nodes:
            # print((node.x, node.y, node.isEdge))
            self.x.append(node.x)
            self.y.append(node.y)
            self.coords.append([node.x, node.y])
            self.edges.append(node.isEdge)
            # print("\ncords:")
            # print(np.array(self.coords))

        # foreach PC
        dx_dXi = np.multiply(dN_dXi, self.x)
        # print()
        # print(dx_dXi)
        self.dx_dXi = [np.sum(dx_dXi[i]) for i in range(4)]
        dx_dEta = np.multiply(dN_dEta, self.x)
        # print()
        # print(dx_dEta)
        self.dx_dEta = [np.sum(dx_dEta[i]) for i in range(4)]
        dy_dXi = np.multiply(dN_dXi, self.y)
        # print()
        # print(dy_dXi)
        self.dy_dXi = [np.sum(dy_dXi[i]) for i in range(4)]
        dy_dEta = np.multiply(dN_dEta, self.y)
        # print()
        # print(dy_dEta)
        self.dy_dEta = [np.sum(dy_dEta[i]) for i in range(4)]


        # print()
        # print(self.dx_dXi)
        # print()
        # print(self.dx_dEta)
        # print()
        # print(self.dy_dXi)
        # print()
        # print(self.dy_dEta)

        J = np.array(
            [
                [self.dx_dXi[i], self.dy_dXi[i], 
                self.dx_dEta[i], self.dy_dEta[i]]
                for i in range(4)
            ]
        ).reshape((4, 2, 2))

        # print(("J", J))

        self.detJ = np.linalg.det(J)
        # print(self.detJ)

        self.invJ = np.array( [np.linalg.inv(J[i]) for i in range(4)])
        # print(np.array(self.invJ[:,0]))
        # print(np.array(self.invJ))



        self.dN_dx = np.zeros((4, 4))
        self.dN_dy = np.zeros((4, 4))

        for i in range(4):
            for j in range(4):
                self.dN_dx[i][j] = (
                    self.invJ[:,0][i][0] * dN_dXi[i][j]
                    + self.invJ[:,0][i][1] * dN_dEta[i][j]
                )
                self.dN_dy[i][j] = (
                    self.invJ[:,1][i][0] * dN_dXi[i][j]
                    + self.invJ[:,1][i][1] * dN_dEta[i][j]
                )

        # print(self.dN_dx)
        # print(self.dN_dy)

    def CalcElements(self):
        self.MatrixH = MatrixH(self).MatrixH
        self.MatrixC = MatrixC(self).MatrixC
        mhbc = MatrixH_BC(self)
        # print(mhbc.MatrixH_BC)
        self.MatrixH_BC = mhbc.MatrixH_BC
        self.detJe = mhbc.detJe
        self.N_bc = mhbc.N_bc
        for i in range(4):
            for j in range(4):
                self.MatrixH[i][j] += self.MatrixH_BC[i][j]
        self.VectorP = VectorP(self).VectorP
        # print("\n\nvecP:")
        # print(self.VectorP)
        # print("\n\n")
        return self
le = LocalElement(
    Element(
        [
            Node(1, 0, 0, 100, True),
            Node(5, 0.25, 0, 100, True),
            Node(6, 0.25, 0.25, 100, False),
            Node(2, 0, 0.25, 100, True),
        ]
    )
)