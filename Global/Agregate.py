import numpy as np


def Argegate(_global: np.ndarray, local: np.ndarray, ids: []):
    for i in range(4):
        for j in range(4):
            _global[ids[i]][ids[j]] += local[i][j]
    return _global


def ArgegateP(_global: np.ndarray, local: np.ndarray, ids: []):
    if isinstance(local, np.ndarray or list):
        for i in range(4):
            _global[ids[i]] += local[i]
    return _global

