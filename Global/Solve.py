import numpy as np
from Data.GlobalData import *
from Local.LocalElement import LocalElement
import Global.Agregate as agr


def solve(grid, t0):
    GlobalH = np.zeros((N_H * N_W, N_H * N_W))
    GlobalC = np.zeros((N_H * N_W, N_H * N_W))
    GlobalP = np.zeros(N_H * N_W)

    for element in grid.elements:
        e = LocalElement(element).CalcElements()
        GlobalH = agr.Argegate(GlobalH, e.MatrixH, element.nodeIds)
        GlobalC = agr.Argegate(GlobalC, e.MatrixC, element.nodeIds)
        GlobalP = agr.ArgegateP(GlobalP, e.VectorP, element.nodeIds)

    # print("\nH:"); print(GlobalH); print("\nC:"); print(GlobalC); print("\nP:"); print(GlobalP); print("\n")

    dTau = simulation_step_time
    GlobalC_dTau = GlobalC / dTau

    H = GlobalH + GlobalC_dTau
    P = np.dot(GlobalC_dTau, t0) + GlobalP

    print("\nH + C/dTau :"); print(H); print("\nP + C/dTau * t0 :"); print(P)

    # H*t1 - P = 0
    t1 = np.linalg.solve(H, P)
    # print("\nt1 :")
    # print(t1)
    return t1
    