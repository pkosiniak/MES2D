import numpy as np
from Structures import Grid, Node, Element
from GlobalData import *
from Solve import solve

np.set_printoptions(precision=3, linewidth=200)

grid = Grid(N_H, N_W, H, W, initial_temperature)

t_list = []
t_list.append(grid.getInitialTemperature())


print("Time[s]\t| Min(t)\t\t| Max(t)")


for i in range(int(simulation_time / simulation_step_time)):
    t_list.append(solve(grid, t_list[-1]))
    print((i + 1) * 50, "\t| ", min(t_list[-1]), "\t| ", max(t_list[-1]))