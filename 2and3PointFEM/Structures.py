from typing import List
import numpy as np


class Node:
    def __init__(self, id, x, y, t, isEdge=False):
        self.id = id
        self.x = x
        self.y = y
        self.t = t
        self.isEdge = isEdge


class Element:
    def __init__(self, nodes: List[Node]):
        self.nodes: List[Node] = nodes
        self.nodeIds: List[int] = [i.id for i in nodes]


class Grid:
    def __init__(
        self,
        n_h: int = 5,
        n_w: int = 4,
        h: float = 2.0,
        w: float = 1.2,
        t_init: int = 20,
    ):
        self.nodesInHeight: int = n_h
        self.nodesInWidth: int = n_w
        self.heightLength: float = h
        self.widthLength: float = w
        self.init_t: int = t_init
        self.nodes = self.createNodes()
        self.elements: List[Element] = []
        self.createNodesIds()
        self.createElements()

    def createNodesIds(self):
        i = 0
        for nj in self.nodes:
            for nk in nj:
                nk.id = i
                i += 1
        return self

    def createNodes(self):
        return [
            [
                Node(
                    0,
                    j * (self.widthLength / (self.nodesInWidth - 1)),
                    i * (self.heightLength / (self.nodesInHeight - 1)),
                    self.init_t,
                    True
                    if i == 0
                    or j == 0
                    or i == self.nodesInHeight - 1
                    or j == self.nodesInWidth - 1
                    else False,
                )
                for i in range(self.nodesInHeight)
            ]
            for j in range(self.nodesInWidth)
        ]

    def createElements(self):
        for i in range(self.nodesInHeight - 1):
            for j in range(self.nodesInWidth - 1):
                self.elements.append(
                    Element(
                        [
                            self.nodes[i][j],
                            self.nodes[i + 1][j],
                            self.nodes[i + 1][j + 1],
                            self.nodes[i][j + 1],
                        ]
                    )
                )
        return self
    
    def getInitialTemperature(self):
        t0 = []
        for ni in self.nodes:
            for nj in ni:
                t0.append(nj.t)

        return np.array(t0)
