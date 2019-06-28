import numpy as np
from Data.Structures import Grid, Node, Element
from Data.GlobalData import *
from Global.Solve import solve

np.set_printoptions(precision=3, linewidth=200)

grid = Grid(N_H, N_W, H, W, initial_temperature)


# print("\n\nNode ID's :")
# print(np.array([[j.id for j in i] for i in grid.nodes]).T)

# print("\n\nElements list :")
# print("Element ID\t| Node ID's")
# for i in range(len(grid.elements)):
#    print(i , "\t\t|", np.array(grid.elements[i].nodeIds))

t_list = []
t_list.append(grid.getInitialTemperature())


print("Time[s]\t| Min(t)\t\t| Max(t)")


for i in range(int(simulation_time / simulation_step_time)):
    t_list.append(solve(grid, t_list[-1]))
    print((i + 1) * 50, "\t| ", min(t_list[-1]), "\t| ", max(t_list[-1]))

#  print("\nminimal temperature:\t", " maximal temperature:")
#  print(min(t_list[-1]), "\t", max(t_list[-1]))
#  print("\nIteration:\t", i)

# t_list = np.array(t_list)
# for i in range(int(simulation_time / simulation_step_time)):
